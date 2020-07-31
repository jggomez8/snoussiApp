from config.wsgi import *
from core.rrhh.models import *
from core.security.models import *
from django.contrib.contenttypes.models import ContentType


def search_content_type(name):
    for i in ContentType.objects.all():
        if i.name.lower() == name.lower():
            return i
    return None


module = Module()
module.type_id = 4
module.name = 'Reportes Diarios'
module.url = '/rrhh/reports/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-chart-pie'
module.description = 'Permite administrar los reportes diarios de los empleados del sistema'
module.save()
print('insertado {}'.format(module.name))
