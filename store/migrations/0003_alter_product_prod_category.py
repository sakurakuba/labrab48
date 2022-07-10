# Generated by Django 4.0.6 on 2022-07-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_prod_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_category',
            field=models.CharField(choices=[('other', 'other'), ('Audio/Video', 'Audio/Video'), ('TVs', 'TVs'), ('Cell Phones', 'Cell Phones')], default='other', max_length=20, verbose_name='prod_category'),
        ),
    ]