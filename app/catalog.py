"""
Catálogo de tipos de producto: mapea el segmento de la URL
(teclados, mouses, auriculares, mousepads) al modelo y formulario
correspondientes. Vive en su propio módulo porque tanto views.py
como cart.py necesitan consultarlo.
"""
from .models import Teclado, Mouse, Auricular, Mousepad
from .forms import TecladoForm, MouseForm, AuricularForm, MousepadForm

PRODUCT_TYPES = {
    'teclados': {
        'model': Teclado,
        'form_class': TecladoForm,
        'singular': 'Teclado',
        'plural': 'Teclados',
    },
    'mouses': {
        'model': Mouse,
        'form_class': MouseForm,
        'singular': 'Mouse',
        'plural': 'Mouses',
    },
    'auriculares': {
        'model': Auricular,
        'form_class': AuricularForm,
        'singular': 'Auricular',
        'plural': 'Auriculares',
    },
    'mousepads': {
        'model': Mousepad,
        'form_class': MousepadForm,
        'singular': 'Mousepad',
        'plural': 'Mousepads',
    },
}
