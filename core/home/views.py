from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.views.generic import TemplateView

from core.security.models import Company


class HomeView(TemplateView):
    template_name = 'panel.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        request.user.set_group_session()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        data = self.get_context_data()
 
       
        return render(request, 'hzt_panel.html', data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Panel de administración'
        context['home'] = True
        return context


