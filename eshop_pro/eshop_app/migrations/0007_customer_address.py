# Generated by Django 5.0 on 2024-08-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0006_customer_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Default Name', max_length=200),
        ),
    ]