from django.core.validators import MinValueValidator
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from store.models import Product, CATEGORY_CHOICES


def index_view(request):
    product = Product.objects.order_by('prod_category', 'prod_name')
    return render(request, 'index.html', {"product": product})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {"product": product})


def product_add(request):
    if request.method == 'GET':
        return render(request, 'add.html', {'categories': CATEGORY_CHOICES})
    else:
        prod_name = request.POST.get('prod_name')
        description = request.POST.get('description')
        prod_category = request.POST.get('prod_category')
        balance = request.POST.get('balance')
        price = request.POST.get('price')
        new_product = Product.objects.create(prod_name=prod_name, description=description, prod_category=prod_category, balance=balance, price=price)
        return redirect('product_view', pk=new_product.pk)


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', {'product': product, 'categories': CATEGORY_CHOICES})
    else:
        product.prod_name = request.POST.get('prod_name')
        product.description = request.POST.get('description')
        product.prod_category = request.POST.get('prod_category')
        product.balance = request.POST.get('balance')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_view', pk=product.pk)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'product': product})
    else:
        product.delete()
        return redirect('index')
