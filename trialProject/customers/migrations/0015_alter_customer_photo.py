# Generated by Django 4.2.7 on 2023-11-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_alter_customer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', max_length=255, null=True, upload_to=''),
        ),
    ]
