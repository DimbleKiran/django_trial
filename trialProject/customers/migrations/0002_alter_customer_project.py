# Generated by Django 4.2.7 on 2023-11-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='project',
            field=models.CharField(max_length=50, unique=True, verbose_name='Project Code'),
        ),
    ]