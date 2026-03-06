from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creado_por = request.user # Asigna al usuario actual
            producto.save()
            return redirect('lista') # Redirige a la tabla
    else:
        form = ProductoForm()
    return render(request, 'stock/crear.html', {'form': form})