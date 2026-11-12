from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

# 1. VISTA BASADA EN FUNCIÓN (FBV) - Para la página de bienvenida
def home(request):
    # Contexto básico que pide la guía
    contexto = {
        'titulo': 'Bienvenido a NexusTech',
        'mensaje': 'La mejor tecnología al alcance de tu bolsillo.'
    }
    return render(request, 'home.html', contexto)

# 2. VISTA BASADA EN CLASE (CBV) - Para el catálogo
class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo.html'
    context_object_name = 'productos' # Así lo llamaremos en el HTML
    
    # QUERYSET (Filtrado y ordenado - Punto 4 y 5 de la guía)
    # Filtramos solo los que tienen stock y ordenamos por precio (lazy evaluation)
    queryset = Producto.objects.filter(stock__gt=0).order_by('precio')