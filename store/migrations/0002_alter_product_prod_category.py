# Generated by Django 4.0.6 on 2022-07-10 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_category',
            field=models.CharField(choices=[('other', 'other'), ('audio/video', 'Audio/Video'), ('tvs', 'TVs'), ('cell', 'Cell Phones')], default='other', max_length=20, verbose_name='prod_category'),
        ),
    ]