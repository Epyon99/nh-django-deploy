from django.db import models
from django.forms import ValidationError


# Create your models here.
class Proveedor(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def clean(self):
        if self.direccion and 'corea del norte' in self.direccion:
            raise ValidationError("Actualmente no se pude comerciar con corea del norte.")

    def __str__(self):
        return str(self.name)


class Producto(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="productos/", null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    proveedor = models.ForeignKey(
        Proveedor, related_name="productos", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.name)


class Almacen(models.Model):
    name = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=250, null=True, blank=True)
    productos = models.ManyToManyField(Producto, related_name="almacenes")
    disponible = models.BooleanField(default=True)
    def __str__(self):
        return str(self.name)
