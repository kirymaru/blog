from django.contrib import admin
from django.urls import path


from . import views

app_name = "users"

urlpatterns = [
    path("registro/", views.UserRegisterView.as_view(), name="registro"),
    path("error/", views.ErrorView.as_view(), name="error"),
    path("inicio_usuarios/", views.LoginUser.as_view(), name="inicio_usuarios"),
]
