# Generated by Django 4.2.7 on 2023-11-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_remove_customer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/', verbose_name='Image'),
        ),
    ]