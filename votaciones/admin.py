from django.contrib import admin
from .models import Edicion, Categoria, Votacion, Opcion


class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 1


@admin.register(Edicion)
class EdicionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "anio", "lugar", "activa")
    list_filter = ("activa",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edicion")
    list_filter = ("edicion",)


@admin.register(Votacion)
class VotacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "abierta")
    list_filter = ("abierta", "categoria__edicion")
    inlines = [OpcionInline]


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ("numero", "nombre", "procedencia", "votacion")
    list_filter = ("votacion",)
