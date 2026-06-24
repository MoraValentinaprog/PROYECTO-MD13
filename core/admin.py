from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Post

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Personalizamos las columnas que se ven en la lista
    list_display = ('username', 'email', 'is_staff')
    # Inyectamos nuestros campos nuevos al panel de edición de Django
    fieldsets = UserAdmin.fieldsets + (
        ('Información del Perfil', {'fields': ('bio', 'avatar')}),
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columnas, barra de búsqueda y filtros laterales para el CRUD
    list_display = ('titulo', 'autor', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha_creacion', 'autor')
