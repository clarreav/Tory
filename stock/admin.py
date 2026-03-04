from django.contrib import admin
from .models import Producto, Categoria


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que verás en la lista principal
    list_display = ('sku', 'nombre', 'cantidad', 'creado_por')

    # Función mágica: asigna el usuario actual al guardar
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el producto es nuevo (no tiene ID)
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Categoria)