import os
import socket
from datetime import *

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone

from config.settings import STATIC_URL, MEDIA_URL
from core.security.choices import *
from core.user.models import User


class Company(models.Model):
    name = models.CharField(verbose_name='Compañia', max_length=50, unique=True)
    system_name = models.CharField(verbose_name='Nombre del Sistema', max_length=50, unique=True)
    image = models.ImageField(verbose_name='Logo', upload_to='company/%Y/%m/%d', null=True, blank=True)
    icon = models.CharField(max_length=500, verbose_name='Icono FontAwesome')
    ruc = models.CharField(verbose_name='Ruc', max_length=13, unique=True, blank=True, null=True)
    phone = models.CharField(verbose_name='Teléfono Convencional', max_length=9, unique=True, blank=True, null=True)
    mobile = models.CharField(verbose_name='Teléfono Celular', max_length=10, unique=True, blank=True, null=True)
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=50, unique=True, blank=True, null=True)
    address = models.CharField(verbose_name='Dirección', max_length=255, blank=True, null=True)
    mission = models.CharField(verbose_name='Misión', max_length=1000, blank=True, null=True)
    vision = models.CharField(verbose_name='Visión', max_length=1000, blank=True, null=True)
    about_us = models.CharField(verbose_name='Quienes Somos', max_length=1000, blank=True, null=True)
    layout = models.IntegerField(default=1, verbose_name='Diseño', blank=True, null=True, choices=layout_options)
    card = models.CharField(max_length=50, verbose_name='Card', choices=card, default=card[0][0])
    navbar = models.CharField(max_length=50, verbose_name='Navbar', choices=navbar, default=navbar[0][0])
    brand_logo = models.CharField(max_length=50, verbose_name='Brand Logo', choices=brand_logo,
                                  default=brand_logo[0][0])
    sidebar = models.CharField(max_length=50, verbose_name='Sidebar', choices=sidebar, default=sidebar[0][0])

    def __str__(self):
        return self.name

    def get_icon(self):
        if self.icon:
            return self.icon
        return 'fa fa-cubes'

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/default/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'
        default_permissions = ()
        permissions = (
            ('view_company', 'Can view Compañia'),
        )
        ordering = ['-id']


class ModuleType(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')
    icon = models.CharField(max_length=100, unique=True, verbose_name='Icono')
    is_active = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['icon'] = self.get_icon()
        return item

    def get_icon(self):
        if self.icon:
            return self.icon
        return 'fa fa-times'

    class Meta:
        verbose_name = 'Tipo de Módulo'
        verbose_name_plural = 'Tipos de Módulos'
        ordering = ['-name']


class Module(models.Model):
    url = models.CharField(max_length=100, verbose_name='Url', unique=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    type = models.ForeignKey(ModuleType, null=True, blank=True, verbose_name='Tipo de Módulo', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descripción')
    icon = models.CharField(max_length=100, verbose_name='Icono', null=True, blank=True)
    image = models.ImageField(upload_to='module/%Y/%m/%d', verbose_name='Imagen', null=True, blank=True)
    is_vertical = models.BooleanField(default=False, verbose_name='Vertical')
    is_active = models.BooleanField(default=True, verbose_name='Estado')
    is_visible = models.BooleanField(default=True, verbose_name='Visible')
    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Tabla')

    def __str__(self):
        return '{} [{}]'.format(self.name, self.url)

    def toJSON(self):
        item = model_to_dict(self)
        item['icon'] = self.get_icon()
        if self.type:
            item['type'] = self.type.toJSON()
        item['icon'] = self.get_icon()
        item['image'] = self.get_image()
        item['content_type_is_null'] = self.content_type is None
        return item

    def get_icon(self):
        if self.icon:
            return self.icon
        return 'fa fa-times'

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/default/empty.png')

    def get_image_icon(self):
        if self.image:
            return self.get_image()
        if self.icon:
            return self.get_icon()
        return '{}{}'.format(STATIC_URL, 'img/default/empty.png')

    def get_type(self):
        if self.type:
            return self.type.name
        return None

    def get_permission(self):
        data = []
        if self.content_type is None:
            data.append({
                'id': self.id,
                'module_id': self.id,
                'content_type_id': 0,
                'name': 'Ver',
                'state': 0,
                'pos': 0,
            })
        else:
            pos = 0
            ids_exclude = []
            for i in Permission.objects.filter(content_type=self.content_type_id).exclude(id__in=ids_exclude):
                name = ''
                if 'add_' in i.codename:
                    name = 'Crear'
                elif 'change_' in i.codename:
                    name = 'Editar'
                elif 'delete_' in i.codename:
                    name = 'Eliminar'
                elif 'view_' in i.codename:
                    name = 'Ver'
                data.append({
                    'id': i.id,
                    'codename': i.codename,
                    'module_id': self.id,
                    'name': name,
                    'content_type_id': i.content_type_id,
                    'state': 0,
                    'pos': pos
                })
                pos += 1
        return data

    def delete(self, using=None, keep_parents=False):
        try:
            os.remove(self.image.path)
        except:
            pass
        super(Module, self).delete()

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['-name']


class GroupModule(models.Model):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    modules = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.modules.name

    class Meta:
        verbose_name = 'Grupo Módulo'
        verbose_name_plural = 'Grupos Módulos'
        ordering = ['-id']


class DatabaseBackups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=datetime.now)
    hour = models.TimeField(default=datetime.now)
    localhost = models.CharField(max_length=100, null=True, blank=True)
    hostname = models.TextField(default=socket.gethostname(), null=True, blank=True)
    archive = models.FileField(upload_to='backup/%Y/%m/%d')

    def __str__(self):
        return self.hostname

    def toJSON(self):
        item = model_to_dict(self)
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        item['hour'] = self.hour.strftime('%H:%M %p')
        item['archive'] = self.get_archive()
        return item

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.localhost = socket.gethostbyname(socket.gethostname())
        except:
            self.localhost = None
        super(DatabaseBackups, self).save()

    def get_archive(self):
        if self.archive:
            return '{0}{1}'.format(MEDIA_URL, self.archive)
        return None

    def delete(self, using=None, keep_parents=False):
        try:
            os.remove(self.archive.path)
        except:
            pass
        super(DatabaseBackups, self).delete()

    class Meta:
        verbose_name_plural = 'Respaldo de BD'
        verbose_name = 'Respaldos de BD'
        default_permissions = ()
        permissions = (
            ('view_databasebackups', 'Can view Respaldos de BD'),
            ('add_databasebackups', 'Can add Respaldos de BD'),
            ('delete_databasebackups', 'Can delete Respaldos de BD'),
        )
        ordering = ['-id']


class AccessUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
    hour = models.TimeField(default=datetime.now)
    localhost = models.TextField()
    hostname = models.TextField(default=socket.gethostname())

    def __str__(self):
        return self.hostname

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.toJSON()
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        item['hour'] = self.hour.strftime('%H:%M %p')
        return item

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.localhost = socket.gethostbyname(socket.gethostname())
        except:
            self.localhost = None
        super(AccessUsers, self).save()

    class Meta:
        verbose_name = 'Acceso del usuario'
        verbose_name_plural = 'Accesos de los usuarios'
        default_permissions = ()
        permissions = (
            ('view_accessusers', 'Can view Acceso del usuario'),
            ('delete_accessusers', 'Can delete Acceso del usuario'),
        )
        ordering = ['-id']
