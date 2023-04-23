"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppRecetas.views import (index, RecetaList, RecetaDetail, RecetaCreate, RecetaUpdate, RecetaDelete, SignUp, Login, Logout)

urlpatterns = [
    path('',index, name="index"),
    path('admin/', admin.site.urls),
    path('receta/list/', RecetaList.as_view(), name="receta-list"),
    path('receta/<pk>/detail', RecetaDetail.as_view(), name="receta-detail"),
    path('receta/create', RecetaCreate.as_view(), name="receta-create"),
    path('receta/<pk>/update', RecetaUpdate.as_view(), name="receta-update"),
    path('receta/<pk>/delete', RecetaDelete.as_view(), name="receta-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
       
]
