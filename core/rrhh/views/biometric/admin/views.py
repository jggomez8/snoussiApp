import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView

from core.rrhh.forms import Biometric
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin


class BiometricListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = Biometric
    template_name = 'biometric/admin/list.html'
    permission_required = 'view_biometric'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Marcaciones'
        return context


class BiometricDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = Biometric
    template_name = 'biometric/admin/delete.html'
    success_url = reverse_lazy('biometric_admin_list')
    permission_required = 'delete_biometric'

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
