import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView

from core.security.mixins import AccessModuleMixin, PermissionModuleMixin
from core.security.models import *


class AccessUsersListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = AccessUsers
    template_name = 'access_users/list.html'
    permission_required = 'view_accessusers'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'delete_access_all':
                AccessUsers.objects.all().delete()
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Accesos de los usuarios'
        return context


class AccessUsersDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = AccessUsers
    template_name = 'access_users/delete.html'
    success_url = reverse_lazy('access_users_list')
    permission_required = 'delete_accessusers'

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
