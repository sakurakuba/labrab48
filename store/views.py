from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from store.forms import SearchForm, ProductForm, ItemInCartForm
from store.models import Product, ItemInCart


class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "product"
    ordering = ["prod_category"]
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Product.objects.filter(Q(prod_name__contains=self.search_value) | Q(description__contains=self.search_value))
        return Product.objects.order_by("prod_name")

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
        context['quantity'] = self.object.balance
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


class CartView(ListView):
    model = ItemInCart
    template_name = "cart.html"
    context_object_name = "items"
    ordering = ["item"]
    paginate_by = 5


class ProductAddToCart(CreateView):
    template_name = 'cart.html'
    form_class = ItemInCartForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.product.pk})








