from django import forms
from app.models import Teclado, Mouse, Auricular, Mousepad


class ProductoFormBase(forms.ModelForm):
    """
    Base compartida por los cuatro formularios de producto.
    Antes cada uno repetía el mismo diccionario de widgets a mano;
    ahora la clase estilo de campo se aplica una sola vez acá y
    cada subclase solo declara su modelo.

    También suma tres campos de imagen opcionales (no son parte del
    modelo): al guardar, la vista los toma y crea las filas de
    ImagenProducto correspondientes.
    """
    imagen_1 = forms.ImageField(required=False, label='Imagen 1')
    imagen_2 = forms.ImageField(required=False, label='Imagen 2')
    imagen_3 = forms.ImageField(required=False, label='Imagen 3')

    class Meta:
        fields = ['nombre', 'tipo', 'descripcion', 'fecha', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name.startswith('imagen_'):
                field.widget.attrs.setdefault('class', 'field-input')
                continue
            css = 'field-textarea' if name == 'descripcion' else 'field-input'
            field.widget.attrs.setdefault('class', css)
        self.fields['descripcion'].widget.attrs.setdefault('rows', 4)
        self.fields['fecha'].widget = forms.DateInput(
            attrs={'class': 'field-input', 'type': 'date'}
        )

    def imagenes_cargadas(self):
        """Las imágenes nuevas que el usuario subió en este envío, en orden."""
        return [
            self.cleaned_data.get('imagen_1'),
            self.cleaned_data.get('imagen_2'),
            self.cleaned_data.get('imagen_3'),
        ]


class TecladoForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Teclado


class MouseForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Mouse


class AuricularForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Auricular


class MousepadForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Mousepad
