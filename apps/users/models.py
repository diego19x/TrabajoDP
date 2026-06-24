"""
Modelo de usuario personalizado para TIENDA - UrbanGear.
Extiende AbstractUser con campos de perfil adicionales.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Usuario de UrbanGear.
    Agrega teléfono, dirección de envío y avatar al usuario estándar de Django.
    """
    phone   = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    address = models.TextField(blank=True, verbose_name='Dirección de envío')
    avatar  = models.ImageField(upload_to='avatars/', blank=True, null=True)

    class Meta:
        verbose_name        = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email
