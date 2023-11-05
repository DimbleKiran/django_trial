from django.db import models


class Mechanical(models.Model):
    gen = (("Male", 'Male'), ("Female", "Female"), ("Unspecified", "Unspecified"))
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=gen, default="Male")
