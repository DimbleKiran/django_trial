# Generated by Django 4.1.5 on 2023-03-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mechanical",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("phone", models.BigIntegerField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Unspecified", "Unspecified"),
                        ],
                        default="Male",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
