from django import forms
from django.forms import ModelForm

from core.rrhh.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EmployeeCreateForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}), label='Nombres',
                                 max_length=25)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
                                label='Apellidos', max_length=25)
    dni = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
                          label='Número de cedula', max_length=10)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}), label='Email',
                            max_length=30)

    dependence = forms.ChoiceField(choices=dependence_choices, widget=forms.Select(
        attrs={
            'class': 'form-control select2',
            'style': 'width: 100%'
        }), label='Dependencia')

    birthdate = forms.DateField(input_formats=['%Y-%m-%d'],
                                widget=forms.TextInput(attrs={
                                    'value': datetime.now().strftime('%Y-%m-%d'),
                                    'class': 'form-control datetimepicker-input',
                                    'id': 'birthdate',
                                    'data-toggle': 'datetimepicker',
                                    'data-target': '#birthdate'
                                }),
                                label='Fecha de nacimiento')

    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select(
        attrs={
            'class': 'form-control select2',
            'style': 'width: 100%'
        }), label='Sexo')

    cant_familiar = forms.CharField(widget=forms.TextInput(attrs={'value': 0}), label='Cant.Familiar')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        del self.fields['password1']
        del self.fields['password2']

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'dni', 'email', 'image', 'gender', 'dependence', 'birthdate', 'cant_familiar'
        exclude = ['password1', 'password2', 'username']


class EmployeeChangeForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}), label='Nombres',
                                 max_length=25)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
                                label='Apellidos', max_length=25)
    dni = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
                          label='Número de cedula', max_length=10)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}), label='Email',
                            max_length=30)

    dependence = forms.ChoiceField(choices=dependence_choices, widget=forms.Select(
        attrs={
            'class': 'form-control select2',
            'style': 'width: 100%'
        }), label='Dependencia')

    birthdate = forms.DateField(input_formats=['%Y-%m-%d'],
                                widget=forms.TextInput(attrs={
                                    'value': datetime.now().strftime('%Y-%m-%d'),
                                    'class': 'form-control datetimepicker-input',
                                    'id': 'birthdate',
                                    'data-toggle': 'datetimepicker',
                                    'data-target': '#birthdate'
                                }),
                                label='Fecha de nacimiento')

    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select(
        attrs={
            'class': 'form-control select2',
            'style': 'width: 100%'
        }), label='Sexo')

    cant_familiar = forms.CharField(widget=forms.TextInput(attrs={}), label='Cant.Familiar')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        del self.fields['password']
        # del self.fields['password2']

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'dni', 'email', 'image', 'gender', 'dependence', 'birthdate', 'cant_familiar'
        exclude = []


class SymptomsEmpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_joined'].widget.attrs['autofocus'] = True

    class Meta:
        model = SymptomsEmp
        fields = '__all__'
        widgets = {
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#date_joined'
            })
        }


class BiometricForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_joined'].widget.attrs['autofocus'] = True

    class Meta:
        model = Biometric
        fields = '__all__'
        widgets = {
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#date_joined'
            })
        }
