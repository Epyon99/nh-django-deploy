from django.urls import path
from .views import create_almacen, edit_almacen
from productos import views

urlpatterns = [
    path('almacen/new/', create_almacen, name='create_almacen'),
    path('almacen/<int:almacen_id>/edit/', edit_almacen, name='edit_almacen'),
    path('listview',views.ProductoListView.as_view(), name ='product_listview'),
    path('detailview/<int:pk>/',views.ProductoView.as_view(), name ='product_detailview'),
    path('updateview/<int:pk>/',views.ProductoUpdateView.as_view(), name ='product_updateview'),
    path('createview/',views.ProductoCreateView.as_view(), name ='product_createview'),
    path('deleteview/<int:pk>/',views.ProductoDeleteView.as_view(), name ='product_deleteview'),
    path('proveedor/new',views.ProveedoresClassView.as_view(),name='proveedor_classview')

]
