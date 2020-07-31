import ast
import json
from datetime import datetime

from django.core import serializers
from django.db import models
from django.forms import model_to_dict

from core.rrhh.choices import *
from core.user.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dependence = models.CharField(choices=dependence_choices, max_length=50, default='administrativa')
    birthdate = models.DateField(default=datetime.now)
    cant_familiar = models.IntegerField(default=0)
    gender = models.CharField(default='hombre', choices=gender_choices, max_length=20)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()

    def get_age(self):
        return datetime.now().year - self.birthdate.year

    def toJSON(self):
        item = model_to_dict(self)
        item['birthdate'] = self.birthdate.strftime('%d-%m-%Y')
        item['dependence'] = {'id': self.dependence, 'name': self.get_dependence_display()}
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['user'] = self.user.toJSON()
        item['age'] = self.get_age()
        return item

    def get_infections(self):
        infections = self.symptomsemp_set.filter(level_infected=True)
        data = [i.toJSON() for i in infections]
        return data

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-id']


class SymptomsEmp(models.Model):
    date_joined = models.DateField(default=datetime.now)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    body_temperature = models.IntegerField(default=0)
    air_death = models.IntegerField(choices=options_choices, default=0)
    dry_cough = models.IntegerField(choices=options_choices, default=0)
    intestinal_discomfort = models.IntegerField(choices=options_choices, default=0)
    headache = models.IntegerField(choices=options_choices, default=0)
    lost_taste = models.IntegerField(choices=options_choices, default=0)
    lost_olfato = models.IntegerField(choices=options_choices, default=0)
    level_infected = models.BooleanField(default=False)

    def __str__(self):
        return self.emp.user.get_full_name()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            validate = 0
            data = json.loads(serializers.serialize('json', [self],  ensure_ascii=False))[0].get('fields')

            del data['body_temperature']
            del data['date_joined']
            del data['emp']

            for k, v in data.items():
                validate += v
            self.level_infected = validate > 2
            self.emp.state = validate <= 2
            self.emp.save()
        except Exception as e:
            print(e)
            pass
        super(SymptomsEmp, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['emp'])
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        return item

    class Meta:
        verbose_name = 'Sintoma Empleado'
        verbose_name_plural = 'Sintomas Empleados'
        ordering = ['-id']


class Biometric(models.Model):
    date_joined = models.DateField(default=datetime.now)
    date_joinedtime = models.DateTimeField(default=datetime.now)
    hour = models.TimeField(default=datetime.now)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hourEntradaM = models.TimeField(auto_now=False, null=True, blank=True)
    hourSalidaM = models.TimeField(auto_now=False, null=True, blank=True)
    hourEntradaV = models.TimeField(auto_now=False, null=True, blank=True)
    hourSalidaV = models.TimeField(auto_now=False, null=True, blank=True)
    hourExtra = models.IntegerField(default=0)

    def __str__(self):
        return self.emp.user.get_full_name()

    class Meta:
        verbose_name = 'Biometrico'
        verbose_name_plural = 'Biometricos'
        ordering = ['-id']
