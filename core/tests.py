from django.test import TestCase
from django.urls import reverse
from .models import Post, Usuario

class BlogTests(TestCase):
    # El método setUp se ejecuta antes de cada prueba para preparar la base de datos virtual
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='evaluador', 
            password='password123',
            email='test@test.com'
        )
        self.post = Post.objects.create(
            titulo='Post para Testing', 
            contenido='Contenido de prueba para validar el ORM', 
            autor=self.usuario
        )

    def test_modelo_post_creacion(self):
        """Verifica que el post se guarde correctamente en la base de datos"""
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.post.titulo, 'Post para Testing')
        self.assertEqual(self.post.autor.username, 'evaluador')

    def test_home_view_status_code(self):
        """Verifica que la página de inicio cargue correctamente (Código HTTP 200)"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post para Testing')
