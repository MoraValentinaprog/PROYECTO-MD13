from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Post

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        # Exigimos los campos base más nuestros campos personalizados
        fields = ('username', 'email', 'bio', 'avatar')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
        # Nota de seguridad: Excluimos el 'autor' intencionalmente.
        # La vista lo inyectará automáticamente para evitar vulnerabilidades.