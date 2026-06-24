"""
Configuración del panel de administración para el catálogo de UrbanGear.
Permite gestionar categorías, productos y variantes desde el admin de Django.
"""
from django.contrib import admin
from .models import Category, Product, ProductVariant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Administración de categorías deportivas de UrbanGear."""
    list_display        = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Administración del catálogo de productos de UrbanGear."""
    list_display        = ['name', 'category', 'price', 'stock', 'available']
    list_filter         = ['available', 'category']
    list_editable       = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields       = ['name', 'description']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    """Administración de variantes de productos (talle y color)."""
    list_display = ['product', 'size', 'color', 'stock', 'extra_price']
    list_filter  = ['size', 'color']
