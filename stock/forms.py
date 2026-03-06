from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Elegimos qué campos mostrar al usuario
        fields = ['sku', 'nombre', 'categoria', 'cantidad', 'stock_minimo', 'costo', 'pvp', 'descripcion']
        # Añadimos estilos de Bootstrap para que se vea bien
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in fields
        }