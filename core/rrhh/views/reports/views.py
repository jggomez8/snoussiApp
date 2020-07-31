import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.rrhh.models import *
from core.security.mixins import AccessModuleMixin


class ReportsView(AccessModuleMixin, TemplateView):
    template_name = 'reports/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', None)
        data = {}
        try:
            if action == 'personal_infected':
                data = self.personal_infected()
            elif action == 'reintegrate':
                emp = Employee.objects.get(pk=request.POST['id'])
                emp.state = True
                emp.save()
                emp.symptomsemp_set.filter().update(level_infected=False)
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def graph_gender(self):
        data = []
        try:
            for i in gender_choices:
                data.append({
                    'name': i[1],
                    'y': Employee.objects.filter(gender=i[0]).count()
                })
        except:
            pass
        return json.dumps(data)

    def graph_dependence(self):
        data = []
        try:
            for i in dependence_choices:
                data.append({
                    'name': i[1],
                    'y': Employee.objects.filter(dependence=i[0]).count()
                })
        except:
            pass
        return json.dumps(data)

    def graph_infected_gender(self):
        data = []
        try:
            for i in gender_choices:
                data.append({
                    'name': i[1],
                    'y': SymptomsEmp.objects.filter(emp__gender=i[0], level_infected=True).count()
                })
        except:
            pass
        return json.dumps(data)

    def graph_infected_areas(self):
        data = []
        try:
            for i in dependence_choices:
                data.append({
                    'name': i[1],
                    'y': SymptomsEmp.objects.filter(emp__dependence=i[0], level_infected=True).count()
                })
        except:
            pass
        return json.dumps(data)

    def personal_infected(self):
        data = []
        notInfected = []
        infected = 0
        epidemiological_fence = 0
        try:
            emps_ids = list(SymptomsEmp.objects.filter(level_infected=True).order_by('emp_id').values_list('emp_id', flat=True))
            for e in Employee.objects.filter().exclude(id__in=emps_ids):
                notInfected.append(e.toJSON())
            for e in Employee.objects.filter(id__in=emps_ids):
                emp = e.toJSON()
                emp['infections'] = e.get_infections()
                isolated_employees = Employee.objects.filter(dependence=e.dependence).count()
                emp['isolated_employees'] = isolated_employees
                emp['cant_total'] = isolated_employees + e.cant_familiar
                epidemiological_fence += (isolated_employees + e.cant_familiar)
                data.append(emp)
            infected = Employee.objects.filter(id__in=emps_ids).count()
        except:
            pass
        info = {
            'table': data,
            'infected': infected,
            'notInfected': notInfected,
            'epidemiological_fence': epidemiological_fence,
        }
        return info

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes Diarios'
        context['graph_gender'] = self.graph_gender()
        context['graph_dependence'] = self.graph_dependence()
        context['graph_infected_gender'] = self.graph_infected_gender()
        context['graph_infected_areas'] = self.graph_infected_areas()
        return context
