import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, RedirectView, TemplateView

from config import settings
from core.login.forms import ResetPasswordForm, ChangePasswordForm
from core.security.functions import get_company
from core.security.models import AccessUsers
from core.user.models import User


class LoginAuthView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        login_different = reverse_lazy('login_different')
        if request.user.is_authenticated and login_different != request.path:
            return HttpResponseRedirect(reverse_lazy('login_authenticated'))
        return super().get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     login(self.request, form.get_user())
    #     if self.request.user.is_authenticated:
    #         AccessUsers(user=self.request.user).save()
    #     return HttpResponseRedirect(self.get_success_url())


class LoginAuthenticatedView(TemplateView):
    template_name = 'login/login_authenticated.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ResetPasswordView(FormView):
    template_name = 'login/reset_pwd.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_pwd(self, id):
        with transaction.atomic():
            url = settings.LOCALHOST if not settings.DEBUG else self.request.META['HTTP_HOST']
            user = User.objects.get(pk=id)
            user.is_change_password = True
            user.save()

            activate_account = '{}{}{}{}'.format('http://', url, '/login/change/password/', user.token)
            message = MIMEMultipart('alternative')
            message['Subject'] = 'Reseteo de contraseña'
            message['From'] = settings.EMAIL_HOST_USER
            message['To'] = user.email

            html = render_to_string('login/send_email.html',
                                    {'user': user,
                                     'link': activate_account,
                                     'comp': get_company()
                                     })
            content = MIMEText(html, 'html')
            message.attach(content)
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(
                settings.EMAIL_HOST_USER, user.email, message.as_string()
            )
            server.quit()

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            users = User.objects.filter(username=request.POST['username'])
            if users.exists():
                user = users[0]
                self.send_email_reset_pwd(user.id)
            else:
                data['error'] = 'El usuario no se encuentra registrado'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de contraseña'
        return context


class ChangePasswordView(FormView):
    template_name = 'login/change_pwd.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = kwargs['pk']
        if User.objects.filter(token=token, is_change_password=True).exists():
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            password = request.POST['password']
            confirmPassword = request.POST['confirmPassword']
            if password == confirmPassword:
                user = User.objects.get(token=kwargs['pk'])
                user.is_change_password = False
                user.set_password(password)
                user.save()
            else:
                data['error'] = 'Las contraseñas deben ser iguales'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambio de contraseña'
        return context


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
