# Generated by Django 4.0.6 on 2022-08-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=60),
        ),
    ]
