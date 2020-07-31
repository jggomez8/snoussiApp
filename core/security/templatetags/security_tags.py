from django.forms import CheckboxInput
from django import template
from core.security.models import Module
from core.security.models import ModuleType
from core.user.models import User

register = template.Library()


@register.filter
def get_modules_type_session(value):
    return ModuleType.objects.filter(module__groupmodule__groups_id=value, is_active=True).distinct().order_by(
        'name')


@register.filter()
def get_modules_vertical_session(type, group):
    return Module.objects.filter(groupmodule__groups_id=group, type_id=type, is_active=True, is_vertical=True).order_by(
        'name')


@register.filter()
def get_modules_horizontal_session(group):
    return Module.objects.filter(groupmodule__groups_id=group, type_id=None, is_active=True,
                                 is_vertical=False).order_by('name')


@register.filter()
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter()
def get_modules(id, grupo):
    return Module.objects.filter(is_active=True, groupmodule__groups_id=grupo, type_id=id).order_by('name')


@register.filter()
def is_empty(data):
    if (data):
        return data
    return '----'


@register.filter()
def convert_letter(title):
    cad = title.replace('_', ' ')
    return cad.upper()


@register.filter()
def get_groups(id):
    cad = ''
    for g in User.objects.get(pk=id).groups.all():
        cad += g.name + ','
    longitude = len(cad) - 1
    return cad[0:longitude]
