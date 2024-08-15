from django.contrib import admin
from .models import Teclado, Mouse, Auricular, Mousepad

# Register your models here.


@admin.register(Teclado)
class TecladoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'precio')

@admin.register(Mouse)
class MouseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'precio')

@admin.register(Auricular)
class AuricularAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'precio')

@admin.register(Mousepad)
class MousepadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'precio')

