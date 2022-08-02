from django.core.validators import MinValueValidator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from store.forms import SearchForm, ProductForm
from store.models import Product, CATEGORY_CHOICES


# def index_view(request):
#     product = Product.objects.order_by('prod_category', 'prod_name')
#     return render(request, 'index.html', {"product": product})
#
#
# def product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'product.html', {"product": product})
#
#
# def product_add(request):
#     if request.method == 'GET':
#         return render(request, 'add.html', {'categories': CATEGORY_CHOICES})
#     else:
#         prod_name = request.POST.get('prod_name')
#         description = request.POST.get('description')
#         prod_category = request.POST.get('prod_category')
#         balance = request.POST.get('balance')
#         price = request.POST.get('price')
#         new_product = Product.objects.create(prod_name=prod_name, description=description, prod_category=prod_category, balance=balance, price=price)
#         return redirect('product_view', pk=new_product.pk)
#
#
# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'update.html', {'product': product, 'categories': CATEGORY_CHOICES})
#     else:
#         product.prod_name = request.POST.get('prod_name')
#         product.description = request.POST.get('description')
#         product.prod_category = request.POST.get('prod_category')
#         product.balance = request.POST.get('balance')
#         product.price = request.POST.get('price')
#         product.save()
#         return redirect('product_view', pk=product.pk)
#
#
# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'delete.html', {'product': product})
#     else:
#         product.delete()
#         return redirect('index')
#

class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "product"
    ordering = ["-created_at"]
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Product.objects.filter(Q(prod_name__contains=self.search_value) | Q(description__contains=self.search_value))
        return Product.objects.order_by("-created_at")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            val = urlencode({'search': self.search_value})
            context['query'] = val
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        return context


class ProductCreate(CreateView):
    template_name = 'add.html'
    form_class = ProductForm


class ProductUpdate(UpdateView):
        template_name = 'update.html'
        form_class = ProductForm
        model = Product


class ProductDelete(DeleteView):
    model = Product
    template_name = "delete.html"
    success_url = reverse_lazy("index")
