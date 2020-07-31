import json

from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.rrhh.forms import EmployeeCreateForm, Employee, EmployeeChangeForm, User
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin

from config import settings


class EmployeeListView(AccessModuleMixin, PermissionModuleMixin, ListView):
    model = Employee
    template_name = 'employee/list.html'
    permission_required = 'view_employee'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('employee_create')
        context['title'] = 'Listado de Empleados'
        return context


class EmployeeCreateView(AccessModuleMixin, PermissionModuleMixin, CreateView):
    model = Employee
    template_name = 'employee/create.html'
    form_class = EmployeeCreateForm
    success_url = reverse_lazy('employee_list')
    permission_required = 'add_employee'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'dni':
                if User.objects.filter(dni=obj):
                    data['valid'] = False
            elif type == 'username':
                if User.objects.filter(username=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'add':
                user = User()
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.dni = request.POST['dni']
                user.email = request.POST['email']
                user.username = user.dni
                user.set_password(user.dni)
                if 'image' in request.FILES:
                    user.image = request.FILES['image']
                user.save()

                emp = Employee()
                emp.user_id = user.id
                emp.gender = request.POST['gender']
                emp.birthdate = request.POST['birthdate']
                emp.dependence = request.POST['dependence']
                emp.cant_familiar = request.POST['cant_familiar']
                emp.save()

                group = Group.objects.get(pk=settings.GROUPS.get('employee'))
                user.groups.add(group)

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
        context['title'] = 'Nuevo registro de un Empleado'
        context['action'] = 'add'
        return context


class EmployeeUpdateView(AccessModuleMixin, PermissionModuleMixin, UpdateView):
    model = Employee
    template_name = 'employee/create.html'
    form_class = EmployeeChangeForm
    success_url = reverse_lazy('employee_list')
    permission_required = 'change_employee'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = EmployeeChangeForm(instance=self.object.user, initial={
            'dependence': self.object.dependence,
            'birthdate': self.object.birthdate,
            'cant_familiar': self.object.cant_familiar,
            'gender': self.object.gender,
        })
        return form

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            id = self.get_object().user.id
            if type == 'dni':
                if User.objects.filter(dni=obj).exclude(id=id):
                    data['valid'] = False
            elif type == 'username':
                if User.objects.filter(username=obj).exclude(id=id):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'edit':
                user = self.get_object().user
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.dni = request.POST['dni']
                user.email = request.POST['email']
                user.username = user.dni
                user.set_password(user.dni)
                if 'image' in request.FILES:
                    user.image = request.FILES['image']
                user.save()

                emp = self.get_object()
                emp.gender = request.POST['gender']
                emp.birthdate = request.POST['birthdate']
                emp.dependence = request.POST['dependence']
                emp.cant_familiar = request.POST['cant_familiar']
                emp.save()

                group = Group.objects.get(pk=settings.GROUPS.get('employee'))
                user.groups.add(group)

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
        context['title'] = 'Edición de un Empleado'
        context['action'] = 'edit'
        return context


class EmployeeDeleteView(AccessModuleMixin, PermissionModuleMixin, DeleteView):
    model = Employee
    template_name = 'employee/delete.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'delete_employee'

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
