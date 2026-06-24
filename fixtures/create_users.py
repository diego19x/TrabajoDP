"""
Script de carga de datos iniciales para TIENDA - UrbanGear.
Crea superusuario y usuarios de prueba con contraseñas reales.

Uso:
    python manage.py shell < fixtures/create_users.py
"""
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from apps.users.models import User

# Superusuario administrador
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@urbangear.com',
        password='Admin1234!',
        first_name='Administrador',
        last_name='UrbanGear',
        phone='+54 11 4000-0001',
        address='Av. Cabildo 1234, Buenos Aires',
    )
    print("✅ Superusuario 'admin' creado (contraseña: Admin1234!)")

# Usuario comprador 1
if not User.objects.filter(username='lucas_runner').exists():
    User.objects.create_user(
        username='lucas_runner',
        email='lucas@example.com',
        password='Lucas1234!',
        first_name='Lucas',
        last_name='Fernández',
        phone='+54 11 5555-1234',
        address='Calle Corrientes 987, CABA',
    )
    print("✅ Usuario 'lucas_runner' creado (contraseña: Lucas1234!)")

# Usuario comprador 2
if not User.objects.filter(username='sofia_fit').exists():
    User.objects.create_user(
        username='sofia_fit',
        email='sofia@example.com',
        password='Sofia1234!',
        first_name='Sofía',
        last_name='Martínez',
        phone='+54 11 6666-5678',
        address='Av. Santa Fe 2200, Palermo, CABA',
    )
    print("✅ Usuario 'sofia_fit' creado (contraseña: Sofia1234!)")

print("\n🎽 Usuarios de TIENDA - UrbanGear creados exitosamente.")
