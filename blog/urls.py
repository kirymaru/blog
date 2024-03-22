from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from users.views import HomeView, LoginUser, logout_usuario

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginUser.as_view(), name="login"),
    path("", HomeView.as_view(), name="index"),
    path("Post/", include("corp.urls")),
    path("Users/", include("users.urls")),
    path("Logout/", login_required(logout_usuario), name="logout"),
]
