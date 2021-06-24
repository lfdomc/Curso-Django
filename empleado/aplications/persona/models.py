from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)
    
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades Empleado"
        
    def __str__(self):
        return str(self.id) + " - " + self.habilidad  

# Create your models here.
class Empleado(models.Model):
## Modelo para Tabla Empleado ###

    JOB_CHOICES = (
         ("0", "CONTADOR"),
         ("1", "ADMINISTRADOR"),
         ("2", "ECONOMISTA"),
         ("3", "OTRO"),


    )
    #Contador
    #Administrador
    first_name = models.CharField("Nombres",max_length=60)
    last_name = models.CharField("Apellidos",max_length=20,unique = True)
    job = models.CharField("Trabajo", max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    avatar = models.ImageField(upload_to="empleado", blank=True, null=True)
    hoja_vida = RichTextField()


    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["first_name"]
        unique_together =("first_name", "last_name")


    
    def __str__(self):
        return str(self.id) + " - " + self.first_name + " - "+ self.last_name 