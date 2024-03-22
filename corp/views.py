from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView,View
from rest_framework import generics, authentication, permissions
from django.conf import settings

from .models import *


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'libreria/PostTemplate/post_detail.html', {'post': post})

def listarPost(request):
        posts=Post.objects.all()
        return render(request,'libreria/PostTemplate/listar_Post.html',{'posts':posts})
    


class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'libreria/PostTemplate/PostForm.html'
    
    def form_valid(self, form):
        form.save()
        return redirect('corp:Post')






def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Post eliminado con éxito.')
    return redirect('corp:Post') 


class SharePostView(View):
    def post(self, request,post_id):
        
        # Obtén el post de la base de datos
        post = Post.objects.get(id=post_id)
        # Obtén el correo electrónico del destinatario desde la solicitud POST
        email = request.POST.get('email')
     
        # Asegúrate de que el correo electrónico del destinatario sea válido
        if email:
            send_mail(
                ' Post',
                f'Título: {post.titulo}\n\nContenido: {post.contenido}',
                settings.EMAIL_HOST_USER, 
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Post compartido con éxito.')
        else:
            messages.error(request, 'No se pudo compartir el post.')

        # Redirige al usuario a la vista Post sin pasar post_id
        return HttpResponseRedirect(reverse('corp:Post'))  
    print='email'