from django.db import models
from .choices import lista_departamentos
from django.contrib.auth.models import User
 
class Departamento(models.Model):
    departamento = models.CharField(max_length = 50, choices = lista_departamentos, default = 'Bogotá', unique = True)
 
    def __str__(self) -> str:
        return '{}'.format(self.departamento)


    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamentos'

 
class Habitante(models.Model):
    cedula = models.PositiveBigIntegerField(unique = True)
    nombres = models.CharField(max_length = 255)
    apellidos = models.CharField(max_length = 255)
    direccion = models.CharField(max_length = 255)
    telefono = models.PositiveBigIntegerField()
    ciudad = models.CharField(max_length = 255)
    departamento = models.ForeignKey(Departamento, related_name='Nombre_Departamento', on_delete = models.CASCADE)
 
    def __str__(self) -> str:
        return '{} | {} {} | {}'.format(self.cedula, self.nombres, self.apellidos, self.departamento)


    class Meta:
        verbose_name = 'Habitante'
        verbose_name_plural = 'Habitantes'
        db_table = 'habitantes'