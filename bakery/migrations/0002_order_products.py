# Generated by Django 3.0.5 on 2020-04-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='bakery.OrderProduct', to='bakery.Product'),
        ),
    ]
