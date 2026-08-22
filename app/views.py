from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .catalog import PRODUCT_TYPES
from .models import ImagenProducto
from .cart import Cart


def inicio(request):
    return render(request, 'app/index.html')


class ProductTypeMixin:
    """Resuelve el tipo de producto (teclado/mouse/etc.) a partir de la URL."""

    def dispatch(self, request, *args, **kwargs):
        tipo = kwargs.get('tipo')
        config = PRODUCT_TYPES.get(tipo)
        if config is None:
            raise Http404('Categoría de producto no encontrada.')
        self.product_type = tipo
        self.product_config = config
        self.model = config['model']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = self.product_type
        context['singular'] = self.product_config['singular']
        context['plural'] = self.product_config['plural']
        return context

    def get_success_url(self):
        return reverse('producto_list', kwargs={'tipo': self.product_type})


class ProductoListView(LoginRequiredMixin, ProductTypeMixin, ListView):
    template_name = 'app/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return self.model.objects.prefetch_related('imagenes').all()


class ProductoDetailView(LoginRequiredMixin, ProductTypeMixin, DetailView):
    template_name = 'app/producto_detail.html'
    context_object_name = 'producto'


def _guardar_imagenes(producto, form):
    """
    Toma las imágenes subidas en el formulario (hasta 3) y las guarda
    como filas de ImagenProducto asociadas al producto. Si el usuario
    subió alguna imagen nueva, se reemplazan las anteriores.
    """
    nuevas = [img for img in form.imagenes_cargadas() if img]
    if not nuevas:
        return
    producto.imagenes.all().delete()
    for orden, archivo in enumerate(nuevas):
        ImagenProducto.objects.create(producto=producto, imagen=archivo, orden=orden)


class ProductoCreateView(LoginRequiredMixin, ProductTypeMixin, CreateView):
    template_name = 'app/producto_form.html'

    def get_form_class(self):
        return self.product_config['form_class']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Nuevo {context['singular']}"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        _guardar_imagenes(self.object, form)
        return response


class ProductoUpdateView(LoginRequiredMixin, ProductTypeMixin, UpdateView):
    template_name = 'app/producto_form.html'

    def get_form_class(self):
        return self.product_config['form_class']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Editar {context['singular']}"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        _guardar_imagenes(self.object, form)
        return response


class ProductoDeleteView(LoginRequiredMixin, ProductTypeMixin, DeleteView):
    template_name = 'app/producto_confirm_delete.html'
    context_object_name = 'producto'


# ---- Carrito de compras ----

def agregar_al_carrito(request, tipo, pk):
    config = PRODUCT_TYPES.get(tipo)
    if config is None:
        raise Http404('Categoría de producto no encontrada.')
    producto = get_object_or_404(config['model'], pk=pk)
    cart = Cart(request)
    cart.add(tipo, producto.pk)
    messages.success(request, f'"{producto.nombre}" se agregó al carrito.')
    return redirect(request.META.get('HTTP_REFERER') or 'producto_list', tipo=tipo)


def ver_carrito(request):
    cart = Cart(request)
    return render(request, 'app/carrito.html', {
        'items': cart.items(),
        'total': cart.total(),
    })


def actualizar_carrito(request, tipo, pk):
    if request.method == 'POST':
        try:
            cantidad = int(request.POST.get('cantidad', 1))
        except ValueError:
            cantidad = 1
        Cart(request).set_quantity(tipo, pk, cantidad)
    return redirect('ver_carrito')


def eliminar_del_carrito(request, tipo, pk):
    Cart(request).remove(tipo, pk)
    return redirect('ver_carrito')


def finalizar_compra(request):
    cart = Cart(request)
    if request.method == 'POST' and cart.count() > 0:
        cart.clear()
        messages.success(request, '¡Gracias por tu compra! Este es un proyecto de portfolio, así que el pago no se procesa de verdad — pero el carrito funcionó de punta a punta.')
        return redirect('ver_carrito')
    return redirect('ver_carrito')
