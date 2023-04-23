from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppRecetas.models import Receta
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin #esto se usa para poder restringir ciertas partes de una vista, para un usuario que no esta registrado

def index(request):
    return render(request, "AppRecetas/index.html")

class RecetaList(ListView):
    model = Receta 

class RecetaDetail(DetailView):
    model = Receta 

class RecetaCreate(LoginRequiredMixin, CreateView):
    model = Receta
    success_url = reverse_lazy("receta-list")
    fields = '__all__'
    
class RecetaUpdate(LoginRequiredMixin, UpdateView):
    model = Receta
    success_url = reverse_lazy("receta-list")
    fields = '__all__'

class RecetaDelete(LoginRequiredMixin, DeleteView):
    model = Receta
    success_url = reverse_lazy("receta-list")  

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('receta-list') 

class Login(LoginView):
    next_page = reverse_lazy("receta-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

