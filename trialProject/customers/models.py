from django.db import models


class Customer(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100, null=False)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=100, null=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=100, null=False)
    age = models.IntegerField(verbose_name="Age", null=False)
    address = models.TextField(verbose_name="Address", max_length=500, null=False)
    photo = models.ImageField(max_length=255, blank=True, null=True)


