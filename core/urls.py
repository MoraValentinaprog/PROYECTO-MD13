from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detalle'), # Nueva ruta
    path('about/', views.AboutView.as_view(), name='about'), # Nueva ruta estática
    path('crear/', views.PostCreateView.as_view(), name='crear_post'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]