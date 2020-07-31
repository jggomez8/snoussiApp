from django.forms import ModelForm
from django import forms

from .models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].required = True
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'password', 'dni', 'email', 'groups', 'image'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese un username'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Ingrese un password'}),
            'groups': forms.SelectMultiple(attrs={'class': 'select2', 'multiple': 'multiple', 'style': 'width:100%'}),
        }
        exclude = ['is_change_password', 'is_active', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()

                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'dni', 'email', 'image'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese un username'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
        }
        exclude = ['is_change_password', 'is_active', 'is_staff', 'user_permissions', 'password', 'date_joined',
                   'last_login', 'is_superuser', 'groups']

    token = forms.CharField(widget=forms.HiddenInput(), required=False)

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

