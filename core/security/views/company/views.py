import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, FormView

from core.security.forms import CompanyForm, Company, TemplateForm
from core.security.mixins import AccessModuleMixin, PermissionModuleMixin


class CompanyUpdateView(AccessModuleMixin, PermissionModuleMixin, UpdateView):
    model = Company
    template_name = 'company/create.html'
    form_class = CompanyForm
    success_url = reverse_lazy('home')
    permission_required = 'view_company'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        comps = Company.objects.filter()
        if comps:
            return comps[0]
        return Company()

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'edit':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de la compañia'
        context['action'] = 'edit'
        return context


class CompanySettingView(AccessModuleMixin, FormView):
    template_name = 'company/setting.html'
    form_class = TemplateForm
    success_url = reverse_lazy('home')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = TemplateForm(instance=self.get_object())
        return form

    def get_object(self, queryset=None):
        comps = Company.objects.filter()
        if comps:
            return comps[0]
        return Company()

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'edit':
                comp = self.get_object()
                comp.layout = request.POST['layout']
                comp.navbar = request.POST['navbar']
                comp.brand_logo = request.POST['brand_logo']
                comp.sidebar = request.POST['sidebar']
                comp.card = request.POST['card']
                comp.save()
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de la plantilla'
        context['action'] = 'edit'
        return context
