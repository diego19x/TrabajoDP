"""
Configuración de URLs para TIENDA - UrbanGear API.

Rutas raíz del sistema:
  - /admin/          → Panel de administración
  - /api/users/      → Registro, login y perfil
  - /api/products/   → Catálogo de productos y categorías
  - /api/cart/       → Carrito de compras
  - /api/orders/     → Órdenes de compra
  - /api/payments/   → Simulación y estado de pagos
  - /api/reviews/    → Reseñas de productos
  - /api/coupons/    → Cupones de descuento
"""
from django.contrib import admin
from django.urls import path, include

# Personalización del panel de administración de TIENDA
admin.site.site_header  = 'UrbanGear — Panel de Administración'
admin.site.site_title   = 'UrbanGear Admin'
admin.site.index_title  = 'Bienvenido al panel de gestión de UrbanGear'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',    include('apps.users.api.urls')),
    path('api/products/', include('apps.products.api.urls')),
    path('api/cart/',     include('apps.cart.api.urls')),
    path('api/orders/',   include('apps.orders.api.urls')),
    path('api/payments/', include('apps.payments.api.urls')),
    path('api/reviews/',  include('apps.reviews.api.urls')),
    path('api/coupons/',  include('apps.coupons.api.urls')),
]
