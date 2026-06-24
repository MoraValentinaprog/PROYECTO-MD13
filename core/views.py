from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import RegistroForm, PostForm

class HomeListView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'

# NUEVA VISTA: Para leer el post completo
class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detalle.html'
    context_object_name = 'post'

# NUEVA VISTA: Página estática "Acerca de"
class AboutView(TemplateView):
    template_name = 'core/about.html'

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/crear_post.html'
    success_url = reverse_lazy('home')
    permission_required = 'core.add_post'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')
