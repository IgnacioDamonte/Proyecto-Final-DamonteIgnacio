# myapp1/urls.py
from django.urls import path
from myapp1 import views


urlpatterns = [
    # Vistas para Teclado
    path('', views.inicio, name='Inicio'),
    path('teclados/', views.teclado_list, name='teclado_list'),
    path('teclado/<int:pk>/', views.teclado_detail, name='teclado_detail'),
    path('teclado/crear/', views.teclado_create, name='teclado_create'),
    path('teclado/<int:pk>/editar/', views.teclado_update, name='teclado_update'),
    path('teclado/<int:pk>/eliminar/', views.teclado_delete, name='teclado_delete'),

    # Vistas para Mouse
    path('mouses/', views.mouse_list, name='mouse_list'),
    path('mouse/<int:pk>/', views.mouse_detail, name='mouse_detail'),
    path('mouse/crear/', views.mouse_create, name='mouse_create'),
    path('mouse/<int:pk>/editar/', views.mouse_update, name='mouse_update'),
    path('mouse/<int:pk>/eliminar/', views.mouse_delete, name='mouse_delete'),

    # Vistas para auricular
    path('auriculares/', views.auricular_list, name='auricular_list'),
    path('auricular/<int:pk>/', views.auricular_detail, name='auricular_detail'),
    path('auricular/crear/', views.auricular_create, name='auricular_create'),
    path('auricular/<int:pk>/editar/', views.auricular_update, name='auricular_update'),
    path('auricular/<int:pk>/eliminar/', views.auricular_delete, name='auricular_delete'),

    # Vistas para mousepad
    path('mousepads/', views.mousepad_list, name='mousepad_list'),
    path('mousepad/<int:pk>/', views.mousepad_detail, name='mousepad_detail'),
    path('mousepad/crear/', views.mousepad_create, name='mousepad_create'),
    path('mousepad/<int:pk>/editar/', views.mousepad_update, name='mousepad_update'),
    path('mousepad/<int:pk>/eliminar/', views.mousepad_delete, name='mousepad_delete'),

   

]