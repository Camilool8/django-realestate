# Generated by Django 4.2.3 on 2023-07-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_property_price_currency_alter_property_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]