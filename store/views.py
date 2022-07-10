from django.shortcuts import render

# Create your views here.
from store.models import Product


def index_view(request):
    product = Product.objects.order_by('-created_at')
    return render(request, 'index.html', {"product": product})
