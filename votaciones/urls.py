from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("categorias/", views.categorias, name="categorias"),
    path("edicion/<int:edicion_id>/categorias/", views.categorias, name="categorias_edicion"),
    path("categoria/<int:categoria_id>/participantes/", views.participantes, name="participantes"),
    path("registro/", views.registro, name="registro"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
