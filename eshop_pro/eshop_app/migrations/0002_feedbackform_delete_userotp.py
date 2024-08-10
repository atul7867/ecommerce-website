# Generated by Django 5.0 on 2024-08-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserOTP',
        ),
    ]