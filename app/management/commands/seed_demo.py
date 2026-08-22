import os
from datetime import date

from django.core.files import File
from django.core.management.base import BaseCommand

from app.catalog import PRODUCT_TYPES
from app.models import ImagenProducto

DEMO_IMAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'demo_images')
DEMO_IMAGES_DIR = os.path.normpath(DEMO_IMAGES_DIR)

# tipo -> lista de productos de ejemplo (nombre, sub-tipo, descripción, precio)
PRODUCTOS_DEMO = {
    'teclados': [
        ('Vortex TKL Mecánico', 'mecanico',
         'Teclado mecánico tamaño compacto (TKL), switches táctiles y retroiluminación RGB por tecla.',
         89999),
        ('Nimbus Membrana Silenciosa', 'membrana',
         'Teclado de membrana pensado para oficina y gaming casual, perfil bajo y tipeo silencioso.',
         34999),
    ],
    'mouses': [
        ('Raptor Gaming Inalámbrico', 'inalambrico',
         'Mouse inalámbrico de baja latencia, sensor óptico de alta precisión y batería de larga duración.',
         52999),
        ('Sensei Óptico Pro', 'optico',
         'Mouse óptico ergonómico para uso diario, ideal para largas jornadas de trabajo.',
         21999),
    ],
    'auriculares': [
        ('Aurora Gaming 7.1', 'gaming',
         'Auriculares gaming con sonido envolvente 7.1, micrófono desmontable y almohadillas de espuma viscoelástica.',
         64999),
        ('Breeze Inalámbrico', 'inalambrico',
         'Auriculares inalámbricos livianos, hasta 20 horas de batería y conexión estable de bajo delay.',
         47999),
    ],
    'mousepads': [
        ('Grid XL Gaming', 'gaming',
         'Mousepad extra grande de tela, superficie de control óptimo y base antideslizante.',
         14999),
        ('Cristal Vidrio Templado', 'vidrio',
         'Mousepad de vidrio templado, deslizamiento rápido y acabado premium.',
         18999),
    ],
}


class Command(BaseCommand):
    help = 'Carga productos de ejemplo (con imágenes y descripción) para ver el catálogo funcionando.'

    def handle(self, *args, **options):
        total_creados = 0
        for tipo, productos in PRODUCTOS_DEMO.items():
            model = PRODUCT_TYPES[tipo]['model']
            for nombre, subtipo, descripcion, precio in productos:
                if model.objects.filter(nombre=nombre).exists():
                    self.stdout.write(f'  ya existe: {nombre}')
                    continue

                producto = model.objects.create(
                    nombre=nombre,
                    tipo=subtipo,
                    descripcion=descripcion,
                    fecha=date.today(),
                    precio=precio,
                )

                for orden in range(1, 4):
                    ruta = os.path.join(DEMO_IMAGES_DIR, f'{tipo}_{orden}.png')
                    if not os.path.exists(ruta):
                        continue
                    with open(ruta, 'rb') as f:
                        ImagenProducto.objects.create(
                            producto=producto,
                            imagen=File(f, name=f'{tipo}_{producto.pk}_{orden}.png'),
                            orden=orden - 1,
                        )

                total_creados += 1
                self.stdout.write(self.style.SUCCESS(f'  creado: {nombre} (${precio})'))

        self.stdout.write(self.style.SUCCESS(f'\nListo — {total_creados} productos de ejemplo cargados.'))
