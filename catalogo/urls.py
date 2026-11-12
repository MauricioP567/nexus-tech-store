from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la FBV con name='home'
    path('', views.home, name='home'),
    # Ruta para la CBV con name='catalogo'
    path('catalogo/', views.ProductoListView.as_view(), name='catalogo'),
]