"""Configuración de la aplicación de productos de TIENDA - UrbanGear."""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name               = 'apps.products'
    label              = 'products'
    verbose_name       = 'Catálogo UrbanGear'
