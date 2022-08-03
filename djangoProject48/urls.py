"""djangoProject48 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from store.views import index_view, product_view, product_add, product_update, product_delete
from store.views import IndexView, ProductCreate, ProductView, ProductUpdate, ProductDelete, ProductAddToCart, CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('add/', ProductCreate.as_view(), name="product_add"),
    path('product/<int:pk>', ProductView.as_view(), name="product_view"),
    path('product/<int:pk>/update', ProductUpdate.as_view(), name="product_update"),
    path('product/<int:pk>/delete', ProductDelete.as_view(), name="product_delete"),
    path('cart/', CartView.as_view(), name="cart_view"),
    path('product/<int:pk>/cart/add', ProductAddToCart.as_view(), name="product_add_to_cart"),
]
