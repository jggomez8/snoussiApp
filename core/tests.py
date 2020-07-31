from config.wsgi import *
from core.rrhh.models import Employee, SymptomsEmp, Biometric
from core.security.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from core.user.models import User


def search_content_type(name):
    for i in ContentType.objects.all():
        if i.name.lower() == name.lower():
            return i
    return None


# company
comp = Company()
comp.name = 'Algorisoft'
comp.system_name = 'AlgoriSoft'
comp.icon = 'fas fa-laptop-code'
comp.ruc = '0928363993'
comp.mobile = '0979014551'
comp.phone = '042977557'
comp.email = 'williamjair94@hotmail.com'
comp.address = 'Cdla.Dager, avda. tumbez y carchi'
comp.mission = 'Sin detalles'
comp.vision = 'Sin detalles'
comp.about_us = 'Sin detalles'
comp.layout = 1
comp.card = 'card-primary'
comp.navbar = 'navbar-dark navbar-primary'
comp.brand_logo = ''
comp.sidebar = 'sidebar-dark-primary'
comp.save()

# module type
type = ModuleType()
type.name = 'Seguridad'
type.icon = 'fas fa-lock'
type.save()
print('insertado {}'.format(type.name))

type = ModuleType()
type.name = 'Usuarios'
type.icon = 'fas fa-users'
type.save()
print('insertado {}'.format(type.name))

type = ModuleType()
type.name = 'Administración'
type.icon = 'fas fa-tools'
type.save()
print('insertado {}'.format(type.name))

type = ModuleType()
type.name = 'RRHH'
type.icon = 'fas fa-user-clock'
type.save()
print('insertado {}'.format(type.name))

# module
module = Module()
module.type_id = 1
module.name = 'Tipos de Módulos'
module.url = '/security/module/type/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-door-open'
module.description = 'Permite administrar los tipos de módulos del sistema'
module.content_type = search_content_type(ModuleType._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 1
module.name = 'Módulos'
module.url = '/security/module/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-th-large'
module.description = 'Permite administrar los módulos del sistema'
module.content_type = search_content_type(Module._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 1
module.name = 'Grupos'
module.url = '/security/group/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-users'
module.description = 'Permite administrar los grupos de usuarios del sistema'
module.content_type = search_content_type(Group._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 2
module.name = 'Accesos'
module.url = '/security/access/users/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-user-secret'
module.description = 'Permite administrar los accesos de los usuarios'
module.content_type = search_content_type(AccessUsers._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 1
module.name = 'Respaldos'
module.url = '/security/database/backups/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-database'
module.description = 'Permite administrar los respaldos de base de datos'
module.content_type = search_content_type(DatabaseBackups._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 3
module.name = 'Compañia'
module.url = '/security/company/update/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-building'
module.description = 'Permite actualizar la información de la compañia'
module.content_type = search_content_type(Company._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 3
module.name = 'Conf. de la plantilla'
module.url = '/security/company/setting/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-tools'
module.description = 'Permite configurar los datos de la plantilla'
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 2
module.name = 'Administradores'
module.url = '/user/admin/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-user'
module.description = 'Permite administrar a los administradores del sistema'
module.content_type = search_content_type(User._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.name = 'Cambiar password'
module.url = '/user/change/password/'
module.is_active = True
module.is_vertical = False
module.is_visible = True
module.icon = 'fas fa-key'
module.description = 'Permite cambiar tu password de tu cuenta'
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.name = 'Editar perfil'
module.url = '/user/change/profile/'
module.is_active = True
module.is_vertical = False
module.is_visible = True
module.icon = 'fas fa-user'
module.description = 'Permite cambiar la información de tu cuenta'
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 4
module.name = 'Empleados'
module.url = '/rrhh/employee/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-user-tag'
module.description = 'Permite administrar a los empleados del sistema'
module.content_type = search_content_type(Employee._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 4
module.name = 'Sintomas de Empleados'
module.url = '/rrhh/symptomsemp/admin/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-laptop-medical'
module.description = 'Permite administrar los sintomas de los empleados del sistema'
module.content_type = search_content_type(SymptomsEmp._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 4
module.name = 'Sintomas de Empleados'
module.url = '/rrhh/symptomsemp/employee/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-laptop-medical'
module.description = 'Permite administrar los sintomas de los empleados del sistema'
module.content_type = search_content_type(SymptomsEmp._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 4
module.name = 'Biométrico'
module.url = '/rrhh/biometric/employee/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'far fa-clock'
module.description = 'Permite administrar las asistencias de los empleados del sistema'
module.content_type = search_content_type(Biometric._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.type_id = 4
module.name = 'Biométrico'
module.url = '/rrhh/biometric/admin/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'far fa-clock'
module.description = 'Permite administrar las asistencias de los empleados del sistema'
module.content_type = search_content_type(Biometric._meta.verbose_name.title())
module.save()
print('insertado {}'.format(module.name))

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

# group
group = Group()
group.name = 'Administrador'
group.save()
print('insertado {}'.format(group.name))

for mod in Module.objects.filter():
    gm = GroupModule()
    gm.modules = mod
    gm.groups = group
    gm.save()

    if mod.content_type is not None:
        for perm in Permission.objects.filter(content_type=mod.content_type):
            group.permissions.add(perm)

# user
u = User()
u.first_name = 'William Dávila'
u.last_name = 'Dávila Vargas'
u.username = 'admin'
u.dni = '0928363993'
u.email = 'davilawilliam93@gmail.com'
u.is_active = True
u.is_superuser = True
u.is_staff = True
u.set_password('hacker94')
u.save()

u.groups.add(group)
