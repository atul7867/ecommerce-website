# Generated by Django 5.0 on 2024-08-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0007_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(blank=True, default='Default Name', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(default='Default Name', max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='order_notes',
            field=models.TextField(blank=True, default='Default Name'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='Default Name', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='postal_zip',
            field=models.CharField(default='Default Name', max_length=20),
        ),
    ]