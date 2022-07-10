from django.core.validators import MinValueValidator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from store.models import Product


def index_view(request):
    product = Product.objects.order_by('prod_category', 'prod_name')
    return render(request, 'index.html', {"product": product})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {"product": product})
