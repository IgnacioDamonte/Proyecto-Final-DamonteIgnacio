# CompuGaming

Catálogo de accesorios gamer (teclados, mouses, auriculares y mousepads)
con alta, baja y modificación de productos, cada uno con hasta 3 fotos,
y un carrito de compras funcional. Cuentas de usuario con avatar.
Backend en Django, sin frameworks de frontend.

## Qué resuelve

- CRUD completo para cuatro tipos de producto, protegido por login, con
  hasta 3 imágenes por producto.
- Carrito de compras basado en sesión de Django (sin JavaScript del
  lado del carrito): agregar, actualizar cantidad, quitar y finalizar
  compra, con el total y el contador siempre actualizados.
- Registro, login, edición de perfil (con avatar) y cambio de contraseña.
- Un solo motor de vistas para las cuatro categorías de producto: en vez
  de repetir la lógica de listar/crear/editar/eliminar una vez por cada
  modelo, las vistas se resuelven dinámicamente según el tipo de producto
  que viene en la URL (`/teclados/`, `/mouses/`, `/auriculares/`,
  `/mousepads/`), reutilizando las mismas cinco vistas genéricas de
  Django para los cuatro.
- Templates genéricos: los mismos cuatro archivos de plantilla (lista,
  detalle, formulario, confirmación de borrado) sirven para las cuatro
  categorías, en vez de mantener un juego de plantillas por modelo.
- Las fotos de producto usan un solo modelo (`ImagenProducto`) enganchado
  a cualquiera de los cuatro tipos mediante una relación genérica de
  Django, en vez de repetir tres campos de imagen en cada modelo.

## Stack

**Backend:** Python, Django 5.1, SQLite, Pillow.

**Frontend:** HTML y CSS propio, sin frameworks — tipografías Sora,
Inter y JetBrains Mono.

## Cómo correrlo localmente

```bash
git clone https://github.com/IgnacioDamonte/Proyecto-Final-DamonteIgnacio.git
cd Proyecto-Final-DamonteIgnacio
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo   # opcional: carga 8 productos de ejemplo con fotos
python manage.py runserver
```

Abrí `http://127.0.0.1:8000`, registrate y ya podés navegar el catálogo,
agregar productos al carrito, o cargar los tuyos propios.

El comando `seed_demo` carga productos de ejemplo con descripciones,
precios y 3 ilustraciones cada uno — pensadas para ver el catálogo
funcionando de una, no fotos reales de producto.

## Estructura

```
app/                   catálogo de productos (Teclado, Mouse, Auricular, Mousepad)
  models.py
  catalog.py            mapa tipo de producto → modelo/formulario, usado por vistas y carrito
  forms.py               formulario base compartido por los cuatro tipos
  views.py                vistas genéricas parametrizadas por tipo de producto
  cart.py                  carrito de compras basado en sesión
  demo_images/              ilustraciones usadas por el comando seed_demo
  management/commands/       comando seed_demo
  templates/app/               4 templates genéricos reutilizados por las 4 categorías
users/                  registro, login, perfil y avatar
entrega-final/          configuración del proyecto (settings, urls)
```

## Decisiones de diseño

- **Por qué un solo set de vistas y no una por modelo:** los cuatro
  modelos de producto comparten exactamente la misma lógica de
  alta/baja/modificación — la única diferencia es qué modelo y qué
  formulario usar. Un diccionario (`catalog.py`) que mapea el tipo de
  producto (de la URL) al modelo y formulario correspondiente resuelve
  lo mismo con una quinta parte del código, y el carrito reutiliza ese
  mismo mapa.
- **Por qué el carrito vive en la sesión y no en la base de datos:** no
  hace falta persistir carritos de usuarios anónimos ni across
  dispositivos para este alcance — la sesión de Django alcanza y evita
  una tabla extra.
- **Por qué CSS propio y no Bootstrap:** el objetivo era practicar
  maquetación real y tener control total sobre el diseño, sin depender
  de clases utilitarias de una librería externa.

## Próximos pasos posibles

- Búsqueda y filtro por tipo dentro de cada categoría.
- Reemplazar las ilustraciones de demo por fotos reales de producto.
- Tests automatizados para las vistas del catálogo y del carrito.
