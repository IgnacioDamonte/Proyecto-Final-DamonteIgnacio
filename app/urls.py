from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),

    # Carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('carrito/<slug:tipo>/<int:pk>/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/<slug:tipo>/<int:pk>/actualizar/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/<slug:tipo>/<int:pk>/eliminar/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    # Catálogo: un solo conjunto de rutas parametrizado por tipo de producto
    # (teclados, mouses, auriculares, mousepads) en vez de un bloque de rutas
    # repetido por modelo.
    path('<slug:tipo>/', views.ProductoListView.as_view(), name='producto_list'),
    path('<slug:tipo>/crear/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('<slug:tipo>/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('<slug:tipo>/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('<slug:tipo>/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
]
