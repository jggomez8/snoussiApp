import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView

from core.rrhh.forms import SymptomsEmp
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin


class SymptomsEmpListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = SymptomsEmp
    template_name = 'symptomsemp/admin/list.html'
    permission_required = 'view_symptomsemp'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Sintomas de Empleados'
        return context


class SymptomsEmpDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = SymptomsEmp
    template_name = 'symptomsemp/admin/delete.html'
    success_url = reverse_lazy('symptomsemp_admin_list')
    permission_required = 'delete_symptomsemp'

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
