import json

from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.security.forms import ModuleForm
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin
from core.security.models import *


class ModuleListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = Module
    template_name = 'module/list.html'
    permission_required = 'view_module'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('module_create')
        context['title'] = 'Listado de Módulos'
        return context


class ModuleCreateView(AccessModuleMixin, PermissionModuleMixin, CreateView):
    model = Module
    template_name = 'module/create.html'
    form_class = ModuleForm
    success_url = reverse_lazy('module_list')
    permission_required = 'add_module'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = ModuleForm()
        form.fields['type'].widget.attrs['disabled'] = True
        return form

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'url':
                if Module.objects.filter(url__iexact=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'add':
                form = ModuleForm(request.POST, request.FILES)
                data = form.save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Módulo'
        context['action'] = 'add'
        return context


class ModuleUpdateView(AccessModuleMixin, PermissionModuleMixin, UpdateView):
    model = Module
    template_name = 'module/create.html'
    form_class = ModuleForm
    success_url = reverse_lazy('module_list')
    permission_required = 'change_module'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = ModuleForm(instance=self.object)
        form.fields['type'].widget.attrs['disabled'] = not self.object.is_vertical
        form.fields['type'].required = self.object.is_vertical
        return form

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            id = self.get_object().id
            obj = self.request.POST['obj'].strip()
            if type == 'url':
                if Module.objects.filter(url__iexact=obj).exclude(pk=id):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'edit':
                form = ModuleForm(request.POST, request.FILES, instance=self.object)
                data = form.save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de una Mòdulo'
        context['action'] = 'edit'
        return context


class ModuleDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = Module
    template_name = 'module/delete.html'
    success_url = reverse_lazy('module_list')
    permission_required = 'delete_module'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notificación de eliminación'
        context['list_url'] = self.success_url
        return context
