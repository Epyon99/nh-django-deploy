from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from .forms import ProveedorForm, ProductoForm, AlmacenForm
from .models import Almacen, Producto, Proveedor
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/accounts/login')
def create_almacen(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            almacen = form.save(commit=False)
            if not almacen.disponible:
                form.add_error('disponible','Un almacen no se puede crear indisponible')
                return render(request,'almacen/almacen_edit.html',{'form':form})
            form.save()
            return redirect('almacen/almacen_list')
    else:
        form = AlmacenForm()
    return render(request, 'almacen/almacen_create.html', {'form': form})

@permission_required('productos.add_almacen',login_url='/accounts/login')
def edit_almacen(request, almacen_id):
    almacen = get_object_or_404(Almacen, id=almacen_id)
    if request.method == 'POST':
        form = AlmacenForm(request.POST, instance=almacen)
        if form.is_valid():
            almacen = form.save(commit=False)
            if not almacen.disponible:
                form.add_error('disponible','Un almacen no se puede crear indisponible')
                return render(request,'almacen/almacen_edit.html',{'form':form})
            form.save()
            return redirect('almacen/almacen_list')
    else:
        form = AlmacenForm(instance=almacen)
    return render(request, 'almacen/almacen_edit.html', {'form': form, 'almacen': almacen})

class ProductoListView(LoginRequiredMixin,ListView):
    model = Producto
    template_name = 'producto/product_list.html'
    login_url = '/accounts/login' # donde autenticar

class ProductoView(DetailView):
    model = Producto
    template_name = 'producto/product_detail.html'

class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/product_form.html'
    success_url = '/productos/listview'
    permission_required = 'productos.add_producto'

    def form_valid(self, form):
        producto = form.save(commit=False)
        is_invalid = False
        if 'prohibido' in producto.name:
            form.add_error('name','El nombre no puede ser la palabra "Prohibido".')
            is_invalid = True
        if float(producto.price) < 5:
            form.add_error('name','El valor del precio no puede ser menor que 5')
            is_invalid = True
        
        if is_invalid:
            return self.form_invalid(form)
        else:
            return super().form_valid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/product_form.html'
    success_url = '/productos/'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/product_delete.html'
    success_url = '/productos/'

class ProveedoresClassView(PermissionRequiredMixin,View):    
    success_url = '/productos/listview'
    permission_required = 'productos.add_proveedor'
    def get(self, request, proveedor_id=None):
        if proveedor_id:
            proveedor = get_object_or_404(Proveedor, id=proveedor_id)
            form =ProveedorForm(instance=proveedor)
            return render(request,'proveedor/proveedor_form.html', {'form':form})
        else:
            form =ProveedorForm()
            return render(request,'proveedor/proveedor_form.html',{'form':form})
    def post(sef,request):
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_listview')
        else:
            return render(request,'proveedor/proveedor_form.html',{'form':form})