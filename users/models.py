from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here


class UserManager(BaseUserManager):
    def create_user(self, nombre, apellidos, email, password, **extra_fields):
        if not email:
            raise ValueError("Falta el Email")
        user = self.model(
            nombre=nombre, apellidos=apellidos, email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, nombre, apellidos, email, password):
        user = self.create_user(nombre, apellidos, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return f'{self.nombre}-{self.apellidos}'