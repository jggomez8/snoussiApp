import json
from datetime import datetime

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.rrhh.forms import SymptomsEmp, SymptomsEmpForm, symptom_choices
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin


class SymptomsEmpListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = SymptomsEmp
    template_name = 'symptomsemp/employee/list.html'
    permission_required = 'view_symptomsemp'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return SymptomsEmp.objects.filter(emp_id=self.request.user.employee.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('symptomsemp_employee_create')
        context['title'] = 'Listado de Sintomas de Empleados'
        return context


class SymptomsEmpCreateView(AccessModuleMixin, PermissionModuleMixin, CreateView):
    model = SymptomsEmp
    template_name = 'symptomsemp/employee/create.html'
    form_class = SymptomsEmpForm
    success_url = reverse_lazy('symptomsemp_employee_list')
    permission_required = 'add_symptomsemp'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        datenow = datetime.now().date()
        if SymptomsEmp.objects.filter(emp_id=self.request.user.employee.id, date_joined=datenow).exists():
            messages.error(request, 'Ya registro una ficha para este día')
            return HttpResponseRedirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def get_symptoms(self):
        data = []
        try:
            for i in symptom_choices:
                data.append({
                    'key': i[0],
                    'name': i[1],
                    'state': 0,
                    'cant': 0
                })
        except:
            pass
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'add':
                with transaction.atomic():
                    symptoms = json.loads(request.POST['symptoms'])
                    sint = SymptomsEmp()
                    sint.emp_id = request.user.employee.id
                    sint.date_joined = datetime.now()
                    sint.body_temperature = symptoms[6].get('cant')
                    sint.air_death = symptoms[0].get('state')
                    sint.dry_cough = symptoms[1].get('state')
                    sint.intestinal_discomfort = symptoms[2].get('state')
                    sint.headache = symptoms[3].get('state')
                    sint.lost_taste = symptoms[4].get('state')
                    sint.lost_olfato = symptoms[5].get('state')
                    sint.save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Sintoma de Empleado'
        context['action'] = 'add'
        context['symptoms'] = json.dumps(self.get_symptoms())
        return context


class SymptomsEmpUpdateView(AccessModuleMixin, PermissionModuleMixin, UpdateView):
    model = SymptomsEmp
    template_name = 'symptomsemp/admin/create.html'
    form_class = SymptomsEmpForm
    success_url = reverse_lazy('symptomsemp_employee_list')
    permission_required = 'change_symptomsemp'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_symptoms(self):
        data = []
        try:
            symptoms = self.get_object()
            data.append({
                'key': symptom_choices[0][0],
                'name': symptom_choices[0][1],
                'state': symptoms.body_temperature,
                'cant': 1
            })
            data.append({
                'key': symptom_choices[1][0],
                'name': symptom_choices[1][1],
                'state': symptoms.air_death,
                'cant': 0
            })
            data.append({
                'key': symptom_choices[2][0],
                'name': symptom_choices[2][1],
                'state': symptoms.dry_cough,
                'cant': 0
            })
            data.append({
                'key': symptom_choices[3][0],
                'name': symptom_choices[3][1],
                'state': symptoms.intestinal_discomfort,
                'cant': 0
            })
            data.append({
                'key': symptom_choices[4][0],
                'name': symptom_choices[4][1],
                'state': symptoms.headache,
                'cant': 0
            })
            data.append({
                'key': symptom_choices[5][0],
                'name': symptom_choices[5][1],
                'state': symptoms.lost_taste,
                'cant': 0
            })
            data.append({
                'key': symptom_choices[6][0],
                'name': symptom_choices[6][1],
                'state': symptoms.lost_olfato,
                'cant': 0
            })
        except:
            pass
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'add':
                with transaction.atomic():
                    sint = self.get_object()
                    symptoms = json.loads(request.POST['symptoms'])
                    date_joined = datetime.now()
                    sint.emp_id = request.user.employee.id
                    sint.date_joined = date_joined
                    sint.body_temperature = symptoms[6].get('cant')
                    sint.air_death = symptoms[0].get('state')
                    sint.dry_cough = symptoms[1].get('state')
                    sint.intestinal_discomfort = symptoms[2].get('state')
                    sint.headache = symptoms[3].get('state')
                    sint.lost_taste = symptoms[4].get('state')
                    sint.lost_olfato = symptoms[5].get('state')
                    sint.save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Sintoma de Empleado'
        context['action'] = 'add'
        context['symptoms'] = json.dumps(self.get_symptoms())
        return context


class SymptomsEmpDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = SymptomsEmp
    template_name = 'symptomsemp/employee/delete.html'
    success_url = reverse_lazy('symptomsemp_employee_list')
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
