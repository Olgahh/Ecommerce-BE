# Generated by Django 3.0.5 on 2020-04-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0008_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
