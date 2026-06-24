"""Configuración de la aplicación de órdenes de TIENDA - UrbanGear."""
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name               = 'apps.orders'
    label              = 'orders'
    verbose_name       = 'Órdenes UrbanGear'
