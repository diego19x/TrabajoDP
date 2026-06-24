"""
Modelo de reseñas de productos para TIENDA - UrbanGear.
Los compradores pueden dejar una valoración (1-5 estrellas) por producto.
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import User
from apps.products.models import Product


class Review(models.Model):
    """
    Reseña de un producto en UrbanGear.
    Cada usuario puede dejar una sola reseña por producto.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating  = models.IntegerField(
                  validators=[MinValueValidator(1), MaxValueValidator(5)],
                  verbose_name='Calificación (1-5 estrellas)'
              )
    comment = models.TextField(verbose_name='Comentario')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Reseña'
        verbose_name_plural = 'Reseñas'
        unique_together     = ('product', 'user')   # 1 reseña por usuario/producto
        ordering            = ['-created']

    def __str__(self):
        return f"{self.user.username} → {self.product.name} ({self.rating}★)"
