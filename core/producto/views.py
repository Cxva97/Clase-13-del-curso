from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')
def detail_product(request, nombre):
    return HttpResponse(f"El producto que tu buscas es {nombre}")
def detail_product_render(request, nombre):
    context= {
        "nombre": nombre
    }
    return render(request, 'detail_product.html', context=context)
def detalle(request, cantidad, descripcion):
    cantidad = 2 * cantidad
    return (HttpResponse(f"El producto es {descripcion} y tenemos {cantidad}"))
def mostrarNombres_render(request, name, surname):
    context={
        "name": name,
        "surname": surname
    }
    return render(request, 'nombre.html', context=context)