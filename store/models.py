from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
CATEGORY_CHOICES = [('other', 'other'), ('Audio/Video', 'Audio/Video'), ('TVs', 'TVs'), ('Cell Phones', 'Cell Phones')]


class Product(models.Model):
    prod_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='prod_name', default='no name')
    description = models.CharField(max_length=2000, verbose_name='description')
    prod_category = models.CharField(max_length=20, null=False, blank=False, choices=CATEGORY_CHOICES, verbose_name='prod_category', default=CATEGORY_CHOICES[0][1])
    balance = models.IntegerField(validators=[MinValueValidator(0)], default=0, verbose_name='balance')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f"{self.id}. {self.prod_name}: price {self.price},  category - {self.prod_category}, balance - {self.balance}"
