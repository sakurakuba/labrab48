from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from .models import Product, ItemInCart


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["prod_name", "description", "prod_category", "balance", "price"]
        widgets = {
            "prod_category": widgets.RadioSelect,
            "description": widgets.Textarea(attrs={"placeholder": "please add description here"})
        }

    def balance_check(self):
        balance = self.cleaned_data.get('balance')
        if int(balance) < 0:
            raise ValidationError("Quantity cannot be 0 when adding new product")
        return balance

    def price_check(self):
        price = self.cleaned_data.get('price')
        if int(price) < 0:
            raise ValidationError("Price cannot be negative")
        return price


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Search')


class ItemInCartForm(forms.ModelForm):
    class Meta:
        model = ItemInCart
        fields = "__all__"
