from django import forms
from .models import Producto, Proveedor, Almacen

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name', 'direccion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'descripcion', 'proveedor','image','price']
    def clean_price(self):
        precio = self.cleaned_data.get('price')
        if (float(precio) <= 0):
            raise forms.ValidationError("El precio debe ser mayor que cero")
        return precio

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['name', 'ubicacion', 'productos','disponible']
        widgets = {
            'productos': forms.CheckboxSelectMultiple()
        }
