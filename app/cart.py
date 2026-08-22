"""
Carrito de compras basado en sesión de Django.

Se guarda como un diccionario simple en request.session, con claves
"tipo:pk" (por ejemplo "teclados:3") y como valor la cantidad. Reutiliza
el mismo diccionario PRODUCT_TYPES de views.py para resolver a qué
modelo corresponde cada ítem — así el carrito funciona para los cuatro
tipos de producto sin necesitar cuatro implementaciones distintas.
"""
from .catalog import PRODUCT_TYPES

CART_SESSION_KEY = 'carrito'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if cart is None:
            cart = {}
            self.session[CART_SESSION_KEY] = cart
        self.cart = cart

    def _key(self, tipo, pk):
        return f"{tipo}:{pk}"

    def add(self, tipo, pk, cantidad=1):
        key = self._key(tipo, pk)
        self.cart[key] = self.cart.get(key, 0) + cantidad
        self.save()

    def set_quantity(self, tipo, pk, cantidad):
        key = self._key(tipo, pk)
        if cantidad <= 0:
            self.cart.pop(key, None)
        else:
            self.cart[key] = cantidad
        self.save()

    def remove(self, tipo, pk):
        self.set_quantity(tipo, pk, 0)

    def clear(self):
        self.cart = {}
        self.save()

    def save(self):
        self.session[CART_SESSION_KEY] = self.cart
        self.session.modified = True

    def items(self):
        """
        Devuelve la lista de productos en el carrito con sus datos
        actuales (nombre, precio, imagen) resueltos desde la base —
        así si el precio de un producto cambia, el carrito siempre
        muestra el precio vigente, no uno viejo guardado a mano.
        """
        resolved = []
        stale_keys = []
        for key, cantidad in self.cart.items():
            tipo, pk = key.split(':')
            config = PRODUCT_TYPES.get(tipo)
            if not config:
                stale_keys.append(key)
                continue
            try:
                producto = config['model'].objects.get(pk=pk)
            except config['model'].DoesNotExist:
                stale_keys.append(key)
                continue
            primera_imagen = producto.imagenes.first()
            resolved.append({
                'tipo': tipo,
                'pk': producto.pk,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'cantidad': cantidad,
                'subtotal': producto.precio * cantidad,
                'imagen': primera_imagen.imagen.url if primera_imagen else None,
            })

        for key in stale_keys:
            self.cart.pop(key, None)
        if stale_keys:
            self.save()

        return resolved

    def total(self):
        return sum(item['subtotal'] for item in self.items())

    def count(self):
        return sum(self.cart.values())
