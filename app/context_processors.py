from .cart import Cart


def carrito(request):
    return {'carrito_count': Cart(request).count()}
