import json

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.security.forms import GroupForm
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin
from core.security.models import *


class GroupListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = Group
    template_name = 'group/list.html'
    permission_required = 'view_group'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'search_permissions':
                data = []
                for i in Permission.objects.filter(group__in=[request.POST['id']]):
                    data.append({
                        'id': i.id,
                        'name': i.name,
                        'codename': i.codename,
                    })
            elif action == 'search_modules':
                data = []
                for i in Module.objects.filter(groupmodule__groups__in=[request.POST['id']]):
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('group_create')
        context['title'] = 'Listado de Grupos'
        return context


class GroupCreateView(AccessModuleMixin, PermissionModuleMixin, CreateView):
    model = Group
    template_name = 'group/create.html'
    form_class = GroupForm
    success_url = reverse_lazy('group_list')
    permission_required = 'add_group'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'name':
                if Group.objects.filter(name__iexact=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def get_permissions(self):
        data = []
        modules = Module.objects.filter().exclude().order_by('name')
        for i in modules:
            info = i.toJSON()
            info['permissions'] = i.get_permission()
            data.append(info)
        return json.dumps(data)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', None)
        data = {}
        try:
            if action == 'add':
                with transaction.atomic():
                    items = json.loads(request.POST['items'])
                    group = Group()
                    group.name = items['name']
                    group.save()

                    modules_pk_post = []
                    for p in items['permissions']:
                        if p['content_type_id'] == 0:
                            modules_pk_post.append(int(p.get('module_id')))
                        elif 'codename' in p:
                            if 'view_' in p['codename']:
                                modules_pk_post.append(int(p.get('module_id')))

                    for pk in modules_pk_post:
                        det = GroupModule()
                        det.groups = group
                        det.modules_id = pk
                        det.save()

                    permissions_pk_post = [int(d.get('id')) for d in items['permissions'] if d['content_type_id'] != 0]

                    for pk in permissions_pk_post:
                        perm = Permission.objects.get(pk=pk)
                        if 'view_' in perm.codename:
                            module = perm.content_type.module_set.all()
                            if module.exists():
                                module = module[0]
                                if not GroupModule.objects.filter(groups_id=group.id, modules_id=module.id).exists():
                                    det = GroupModule()
                                    det.groups_id = group.id
                                    det.modules_id = module.id
                                    det.save()
                        group.permissions.add(perm)
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['permissions'] = self.get_permissions()
        context['title'] = 'Nuevo registro de un Grupo'
        context['action'] = 'add'
        return context


class GroupUpdateView(AccessModuleMixin, PermissionModuleMixin, UpdateView):
    model = Group
    template_name = 'group/create.html'
    form_class = GroupForm
    success_url = reverse_lazy('group_list')
    permission_required = 'change_group'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            id = self.get_object().id
            obj = self.request.POST['obj'].strip()
            if type == 'name':
                if Group.objects.filter(name__iexact=obj).exclude(id=id):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def get_permissions(self):
        data = []
        modules = Module.objects.filter().exclude().order_by('name')
        group = Group.objects.get(pk=self.get_object().id)
        for m in modules:
            permissions = []
            if m.content_type is None:
                obj = m.get_permission()[0]
                obj['state'] = 1 if GroupModule.objects.filter(modules_id=m.id, groups_id=group.id).exists() else 0
                permissions.append(obj)
            else:
                for p in m.get_permission():
                    perm = p
                    if group.permissions.filter(id=p['id'], group__in=[group]).exists():
                        perm['state'] = 1
                    permissions.append(perm)
            item = m.toJSON()
            item['permissions'] = permissions
            data.append(item)
        return json.dumps(data)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', None)
        data = {}
        try:
            if action == 'edit':
                with transaction.atomic():
                    items = json.loads(request.POST['items'])
                    group = self.get_object()
                    group.name = items['name']
                    group.save()

                    modules_pk_post = []
                    for p in items['permissions']:
                        if p['content_type_id'] == 0:
                            modules_pk_post.append(int(p.get('module_id')))
                        elif 'codename' in p:
                            if 'view_' in p['codename']:
                                modules_pk_post.append(int(p.get('module_id')))
                    modules_pk_post = sorted(list(dict.fromkeys(modules_pk_post)))
                    modules_pk_current = sorted(list(group.groupmodule_set.values_list('modules_id', flat=True)))
                    modules_pk_remove = sorted([m for m in modules_pk_current if m not in modules_pk_post])
                    modules_pk_insert = sorted([m for m in modules_pk_post if m not in modules_pk_current])
                    if len(modules_pk_remove):
                        group.groupmodule_set.filter(modules_id__in=modules_pk_remove).delete()
                    for pk in modules_pk_insert:
                        det = GroupModule()
                        det.groups = group
                        det.modules_id = pk
                        det.save()

                    permissions_pk_post = sorted([int(d.get('id')) for d in items['permissions'] if d['content_type_id'] != 0])
                    permissions_pk_current = sorted(list(group.permissions.values_list('id', flat=True)))
                    permissions_pk_remove = sorted([m for m in permissions_pk_current if m not in permissions_pk_post])
                    permissions_pk_insert = sorted([m for m in permissions_pk_post if m not in permissions_pk_current])

                    if len(permissions_pk_remove):
                        for p in permissions_pk_remove:
                            perm = Permission.objects.get(pk=p)
                            group.permissions.remove(perm)

                    for pk in permissions_pk_insert:
                        perm = Permission.objects.get(pk=pk)
                        if 'view_' in perm.codename:
                            module = perm.content_type.module_set.all()
                            if module.exists():
                                module = module[0]
                                if not GroupModule.objects.filter(groups_id=group.id, modules_id=module.id).exists():
                                    det = GroupModule()
                                    det.groups_id = group.id
                                    det.modules_id = module.id
                                    det.save()
                        group.permissions.add(perm)

            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['permissions'] = self.get_permissions()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de un Grupo'
        context['action'] = 'edit'
        return context


class GroupDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = Group
    template_name = 'group/delete.html'
    success_url = reverse_lazy('group_list')
    permission_required = 'delete_group'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            group = self.get_object()
            group.groupmodule_set.all().delete()
            group.permissions.clear()
            group.delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notificación de eliminación'
        context['list_url'] = self.success_url
        return context