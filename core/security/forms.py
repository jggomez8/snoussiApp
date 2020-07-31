from django import forms
from django.forms import ModelForm

from .models import *


class ModuleTypeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = ModuleType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'icon': forms.TextInput(attrs={'placeholder': 'ingrese un icono de font awesone'}),
        }
        exclude = []

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


class ModuleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['autofocus'] = True

    class Meta:
        model = Module
        fields = '__all__'
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'Ingrese una url'}),
            'type': forms.Select(attrs={'class': 'form-control select2', 'required': False, 'style': 'width:100%'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese una descripción'}),
            'icon': forms.TextInput(attrs={'placeholder': 'ingrese un icono de font awesone'}),
            'content_type': forms.Select(
                attrs={'class': 'form-control select2', 'style': 'width:100%'}),
        }
        exclude = []

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


class GroupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Group
        fields = 'name',
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
        }
        exclude = ['modules']


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'system_name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre del sistema'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'icon': forms.TextInput(attrs={'placeholder': 'Ingrese un icono de font awesome'}),
            'layout': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'navbar': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'brand_logo': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'card': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'sidebar': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'proprietor': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del propietario'}),
            'ruc': forms.TextInput(attrs={'placeholder': 'Ingrese un ruc'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono convencional'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono celular'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese un email'}),
            'schedule': forms.TextInput(attrs={'placeholder': 'Ingrese un horario'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            'mission': forms.Textarea(attrs={'placeholder': 'Ingrese una misión', 'rows': 3, 'cols': 3}),
            'vision': forms.Textarea(attrs={'placeholder': 'Ingrese una visión', 'rows': 3, 'cols': 3}),
            'about_us': forms.Textarea(
                attrs={'placeholder': 'Ingrese una decripción de acerca de nosotros', 'rows': 3, 'cols': 3}),
        }
        exclude = []

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


class TemplateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['layout'].widget.attrs['autofocus'] = True

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'layout': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'navbar': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'brand_logo': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'card': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
            'sidebar': forms.Select(attrs={'class': 'form-control select2', 'style': 'width:100%'}),
        }
        exclude = ['system_name', 'name', 'icon', 'ruc', 'phone', 'mobile', 'email', 'address', 'mission', 'vision',
                   'about_us', 'image']

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
