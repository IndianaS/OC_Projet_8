# Generated by Django 3.0.5 on 2020-04-23 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_favorite_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='id_compared',
        ),
    ]