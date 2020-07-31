import ast
import json

from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from core.rrhh.forms import Biometric, BiometricForm, SymptomsEmp
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin

from datetime import datetime, timedelta


class BiometricListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = Biometric
    template_name = 'biometric/employee/list.html'
    permission_required = 'view_biometric'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Biometric.objects.filter(emp_id=self.request.user.employee.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('biometric_employee_create')
        context['title'] = 'Listado de Marcaciones'
        return context


class BiometricCreateView(AccessModuleMixin, PermissionModuleMixin, CreateView):
    model = Biometric
    template_name = 'biometric/employee/create.html'
    form_class = BiometricForm
    success_url = reverse_lazy('biometric_employee_list')
    permission_required = 'add_biometric'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'add':
                horary = request.POST['horary']
                emp = request.user.employee
                end_date = datetime.now()
                start_date = end_date - timedelta(days=3)
                sintomas = SymptomsEmp.objects.filter(emp=emp, date_joined__range=[start_date, end_date])
                validate = 0
                if sintomas.exists():
                    sint = json.loads(serializers.serialize('json', [sintomas[0]], ensure_ascii=False))[0].get('fields')

                    del sint['body_temperature']
                    del sint['date_joined']
                    del sint['emp']

                    for k, v in sint.items():
                        validate += v

                if validate > 2:
                    data = {
                        'error': 'El empleado tiene sintomas de covid 19 desde hace 3 días, no pudede registrarse su asistencia. Debe ser atendido'}
                else:
                    h = Biometric.objects.filter(emp_id=emp.id, date_joined=end_date)
                    if h.exists():
                        h = h[0]
                    else:
                        h = Biometric()
                    h.emp_id = emp.id
                    hour = datetime.now().strftime('%H:%M')
                    if horary == 'horaEntradaM':
                        h.hourEntradaM = hour
                    elif horary == 'horaSalidaM':
                        h.hourSalidaM = hour
                    elif horary == 'horaEntradaV':
                        h.hourEntradaV = hour
                    elif horary == 'horaSalidaV':
                        h.hourlidaV = hour
                    h.save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de una Asistencia'
        context['action'] = 'add'
        return context
