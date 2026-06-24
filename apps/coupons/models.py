"""
Modelo de cupones de descuento para TIENDA - UrbanGear.
Permite crear promociones con porcentaje de descuento y vigencia limitada.
"""
from django.db import models
from django.utils import timezone


class Coupon(models.Model):
    """
    Cupón de descuento en UrbanGear.
    Valida vigencia, estado activo y límite de usos antes de aplicarse.
    """
    code       = models.CharField(max_length=50, unique=True, verbose_name='Código')
    discount   = models.DecimalField(
                     max_digits=5, decimal_places=2,
                     help_text='Porcentaje de descuento: 15.00 = 15%'
                 )
    active     = models.BooleanField(default=True, verbose_name='Activo')
    valid_from = models.DateTimeField(verbose_name='Válido desde')
    valid_to   = models.DateTimeField(verbose_name='Válido hasta')
    max_uses   = models.PositiveIntegerField(default=100, verbose_name='Usos máximos')
    used_count = models.PositiveIntegerField(default=0, verbose_name='Veces usado')

    class Meta:
        verbose_name        = 'Cupón'
        verbose_name_plural = 'Cupones'

    def is_valid(self):
        """Verifica si el cupón está activo, vigente y con usos disponibles."""
        now = timezone.now()
        return (
            self.active
            and self.valid_from <= now <= self.valid_to
            and self.used_count < self.max_uses
        )

    def __str__(self):
        return f"{self.code} ({self.discount}%)"
