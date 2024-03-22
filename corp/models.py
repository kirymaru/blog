from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        "Titulo del Post", max_length=100, null=False, blank=False
    )
    contenido = models.CharField(
        "Contenido del Post", max_length=500, null=False, blank=True
    )
    pub_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo
