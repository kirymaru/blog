from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido', )
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el título del post',
                }
            ),
            'contenido': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el contenido del post',
                }
            ),
     
        }
