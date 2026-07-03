
# Create your models here.
from django.db import models 
from ckeditor.fields import RichTextField

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del curso")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='cursos/', verbose_name="Imagen del curso")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio (MXN)")
    cupo_disponible = models.IntegerField(verbose_name="Cupo disponible")
    activo = models.BooleanField(default=True, verbose_name="¿Curso activo?")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre
    

class Actividad(models.Model):
    clave_actividad = models.CharField(max_length=12, verbose_name="Clave")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    descripcion = RichTextField(verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
        return self.clave_actividad