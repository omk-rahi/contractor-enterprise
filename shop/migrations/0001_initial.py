# Generated by Django 5.1.4 on 2025-02-04 04:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Pre-built PC', 'Pre-built PC'), ('Refurbished Laptops & PC', 'Refurbished Laptops & PC'), ('PC Components', 'PC Components'), ('Monitors', 'Monitors'), ('CCTV Cameras', 'CCTV Cameras'), ('Software', 'Software'), ('Peripherals', 'Peripherals')], max_length=50)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Created'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled'), ('delivered', 'Delivered')], default='Created', max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('COD', 'COD'), ('Online', 'Online')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('rejected', 'Rejected')], max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('warranty_periods', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('is_primary', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('freeze', 'Freeze'), ('sold', 'Sold')], default='available', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.product')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.productstock')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='shop.product')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.specification')),
            ],
        ),
    ]
