
# Register your models here.
from django.contrib import admin
from .models import Actividad, Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cupo_disponible', 'activo', 'fecha_creacion')
    list_filter = ('activo', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)  # de más reciente a más antigua


class AdministrarActividad(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('clave_actividad', 'curso', 'created')
    search_fields = ('clave_actividad', 'curso__nombre')
    date_hierarchy = 'created'
    list_filter = ('curso',)

admin.site.register(Actividad, AdministrarActividad)