from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm, LoginForm
from .models import User


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'libreria/PostTemplate/listar_Post.html'

class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        user = form.instance 
        message = f'¡Hola {user.nombre}! Gracias por registrarte '
        send_mail(
            'Bienvenido a nuestra plataforma',
            message,
            settings.EMAIL_HOST_USER, 
            [user.email],
            fail_silently=False,
             )
        login(self.request, user)
        return redirect('users:inicio_usuarios')

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('corp:Post')

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


 

          

class ErrorView(TemplateView):
    template_name = 'users/error_actualizar_clave.html'
    login_url = reverse_lazy('cuentas:login')
