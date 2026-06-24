# TIENDA — UrbanGear API

> API REST de comercio electrónico deportivo, construida con Django 5.2 + Django REST Framework.

---

## 🏃 Descripción

**UrbanGear** es una plataforma de ventas online de artículos deportivos que permite:

- Explorar un catálogo de productos con variantes de talle y color
- Gestionar carritos de compra (usuarios registrados y sesiones anónimas)
- Realizar órdenes con control de estado completo
- Aplicar cupones de descuento porcentual
- Simular pagos con Stripe y MercadoPago
- Dejar reseñas y valoraciones de productos

---

## ⚙️ Requisitos

- Python 3.12+
- pip

---

## 🚀 Instalación y puesta en marcha

### 1. Clonar y configurar entorno virtual

```bash
cd TIENDA
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements/base.txt
```

### 3. Aplicar migraciones

```bash
python manage.py migrate
```

### 4. Crear usuarios de prueba

```bash
python manage.py shell < fixtures/create_users.py
```

### 5. Cargar datos de ejemplo (categorías, productos, cupones)

```bash
python manage.py loaddata fixtures/initial_data.json
```

> ⚠️ Si el fixture incluye usuarios, primero ejecutar el paso 4 y omitir los usuarios del fixture, o usar solo el script del paso 4.

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

La API estará disponible en: **http://127.0.0.1:8000/**

---

## 🔑 Usuarios de prueba

| Usuario        | Contraseña   | Rol            |
|----------------|--------------|----------------|
| `admin`        | `Admin1234!` | Superusuario   |
| `lucas_runner` | `Lucas1234!` | Comprador      |
| `sofia_fit`    | `Sofia1234!` | Comprador      |

---

## 🗂 Estructura del proyecto

```
TIENDA/
├── config/                    # Configuración de Django
│   ├── settings.py            # Ajustes principales
│   ├── urls.py                # Rutas raíz
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── users/                 # Registro, login y perfil
│   ├── products/              # Catálogo, categorías y variantes
│   ├── cart/                  # Carrito de compras
│   ├── orders/                # Órdenes de compra
│   ├── payments/              # Simulación de pagos
│   ├── reviews/               # Reseñas de productos
│   └── coupons/               # Cupones de descuento
├── fixtures/
│   ├── initial_data.json      # Datos de ejemplo (productos, categorías, cupones)
│   └── create_users.py        # Script para crear usuarios con contraseñas
├── requirements/
│   └── base.txt               # Dependencias Python
├── .env                       # Variables de entorno
└── manage.py
```

---

## 📡 Endpoints disponibles

### Autenticación
| Método | Ruta                       | Descripción                        |
|--------|----------------------------|------------------------------------|
| POST   | `/api/users/register/`     | Registro de nuevo usuario          |
| POST   | `/api/users/login/`        | Obtener token JWT                  |
| POST   | `/api/users/token/refresh/`| Renovar token de acceso            |
| GET    | `/api/users/profile/`      | Ver perfil del usuario             |

### Catálogo
| Método | Ruta                                    | Descripción                    |
|--------|-----------------------------------------|--------------------------------|
| GET    | `/api/products/categories/`             | Listar categorías              |
| GET    | `/api/products/products/`               | Listar productos               |
| GET    | `/api/products/products/<slug>/`        | Detalle de producto            |
| GET    | `/api/products/products/<slug>/variantes/` | Variantes del producto      |

### Carrito
| Método | Ruta                          | Descripción              |
|--------|-------------------------------|--------------------------|
| GET    | `/api/cart/`                  | Ver carrito actual       |
| POST   | `/api/cart/add/`              | Agregar producto         |
| PATCH  | `/api/cart/update/<id>/`      | Actualizar cantidad      |
| DELETE | `/api/cart/remove/<id>/`      | Eliminar ítem            |
| DELETE | `/api/cart/clear/`            | Vaciar carrito           |

### Órdenes
| Método | Ruta                       | Descripción              |
|--------|----------------------------|--------------------------|
| GET    | `/api/orders/`             | Historial de órdenes     |
| POST   | `/api/orders/create/`      | Confirmar compra         |
| GET    | `/api/orders/<id>/`        | Detalle de orden         |
| PATCH  | `/api/orders/<id>/cancel/` | Cancelar orden           |

### Pagos
| Método | Ruta                              | Descripción              |
|--------|-----------------------------------|--------------------------|
| POST   | `/api/payments/simulate/`         | Simular pago aprobado    |
| GET    | `/api/payments/<order_id>/status/`| Estado del pago          |

### Reseñas
| Método | Ruta                                    | Descripción              |
|--------|-----------------------------------------|--------------------------|
| GET    | `/api/reviews/<product_slug>/`          | Ver reseñas              |
| POST   | `/api/reviews/<product_slug>/`          | Publicar reseña          |
| DELETE | `/api/reviews/<product_slug>/<id>/`     | Eliminar reseña propia   |

### Cupones
| Método | Ruta                  | Descripción              |
|--------|-----------------------|--------------------------|
| POST   | `/api/coupons/apply/` | Aplicar cupón            |
| DELETE | `/api/coupons/remove/`| Quitar cupón             |

---

## 🎟️ Cupones de prueba

| Código          | Descuento | Vigencia              |
|-----------------|-----------|-----------------------|
| `BIENVENIDO15`  | 15%       | Todo 2024-2026        |
| `SUMMER2024`    | 20%       | Junio–Agosto 2024-26  |
| `FITPRO10`      | 10%       | Todo 2024-2026        |

---

## 🗄️ Base de datos

El proyecto usa **SQLite** por defecto (archivo `db.sqlite3`).

Para migrar a **PostgreSQL** en producción, editar `.env`:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=tienda_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```

---

*TIENDA - UrbanGear API — Proyecto académico de comercio electrónico deportivo*
