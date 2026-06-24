"""Configuración de la aplicación de pagos de TIENDA - UrbanGear."""
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name               = 'apps.payments'
    label              = 'payments'
    verbose_name       = 'Pagos UrbanGear'
