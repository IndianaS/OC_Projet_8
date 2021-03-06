# Generated by Django 3.0.6 on 2020-05-14 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name_fr', models.CharField(max_length=500)),
                ('brands', models.CharField(max_length=200)),
                ('nutrition_grade_fr', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=500)),
                ('image_url', models.CharField(max_length=500)),
                ('image_nutrition_url', models.CharField(max_length=500)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('store', models.ManyToManyField(to='products.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_as_product', to='products.Product', verbose_name='Produit substitué')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_as_substitute', to='products.Product', verbose_name='Substitut proposé')),
            ],
        ),
    ]
