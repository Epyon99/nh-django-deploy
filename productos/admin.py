from django.contrib import admin

from productos.models import Almacen, Producto, Proveedor

# Register your models here.
admin.register(Proveedor)
admin.register(Producto)
admin.register(Almacen)