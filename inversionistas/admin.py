from django.contrib import admin
from .models import Inversionista

@admin.register(Inversionista)
class InversionistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'numeroDocumento', 'email', 'activo')
    search_fields = ('nombre', 'apellido', 'numeroDocumento', 'email')
    list_filter = ('activo',)