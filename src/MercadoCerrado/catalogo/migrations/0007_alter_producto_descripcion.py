# Generated by Django 4.0.6 on 2022-08-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_producto_precio_currency_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]