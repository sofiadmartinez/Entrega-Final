from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppRecetas.models import Receta, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render (request, "AppRecetas/about.html")

def index(request):
    context = {
        "recetas": Receta.objects.all()
    }
    return render(request, "AppRecetas/index.html", context)

class RecetaList(ListView):
    model = Receta
    context_object_name="posts"

class RecetaDetail(DetailView):
    model = Receta 

class RecetaCreate(LoginRequiredMixin, CreateView):
    model = Receta
    success_url = reverse_lazy("receta-list")
    fields = '__all__'
    
class RecetaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    success_url = reverse_lazy("receta-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Receta.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "AppRecetas/not_found.html")


class RecetaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receta
    success_url = reverse_lazy("receta-list")  

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Receta.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "AppRecetas/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('receta-list') 

class Login(LoginView):
    next_page = reverse_lazy("receta-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy("receta-list")

class MensajeList(LoginRequiredMixin,ListView):
    model = Mensaje
    context_object_name= "mensajes"    

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()