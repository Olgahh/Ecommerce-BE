# Generated by Django 3.0.5 on 2020-04-15 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0011_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
