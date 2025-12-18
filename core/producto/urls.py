from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="productosmain") ,
    path('id/<str:nombre>/',views.detail_product_render , name="detailproduct"),
    path('detalle/<int:cantidad>/<str:descripcion>', views.detalle, name="detalle"),
    path('<str:name>/<str:surname>/', views.mostrarNombres_render, name= "mostrarNombre")
]