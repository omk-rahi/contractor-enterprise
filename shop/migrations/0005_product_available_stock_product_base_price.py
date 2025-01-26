# Generated by Django 5.1.4 on 2025-01-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_product_product_type_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='base_price',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
