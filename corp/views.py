from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView,View
from django.conf import settings
from .forms import PostForm
from .models import *


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'libreria/PostTemplate/post_detail.html', {'post': post})

def listarPost(request):
        posts=Post.objects.all()
        return render(request,'libreria/PostTemplate/listar_Post.html',{'posts':posts})
    


class PostCreateView(FormView):
    template_name = 'libreria/PostTemplate/PostForm.html'
    form_class = PostForm
    success_url = reverse_lazy('corp:Post') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect(self.success_url)






@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('corp:Post') # Redirige al usuario a la página principal si no es el autor
    post.delete()
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