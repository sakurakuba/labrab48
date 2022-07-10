from django.contrib import admin

# Register your models here.
from store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'prod_name', 'prod_category', 'balance', 'price']
    list_display_links = ['prod_name']
    list_filter = ['balance']
    search_fields = ['prod_name', 'prod_category']
    fields = ['prod_name', 'description', 'prod_category', 'balance', 'price', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
