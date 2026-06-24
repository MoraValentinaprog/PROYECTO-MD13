from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Heredamos todo de Django (nombre, email, password) y le sumamos nuestros campos:
    bio = models.TextField(max_length=500, blank=True)
    # Nota: Para ImageField luego instalaremos 'Pillow', por ahora dejamos la estructura armada
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordenamos los posts para que los más nuevos salgan primero
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
