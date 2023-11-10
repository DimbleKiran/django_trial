from django.db import models


class Customer(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100, null=False)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=100, null=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=100, null=False)
    age = models.IntegerField(verbose_name="Age", null=False)
    address = models.TextField(verbose_name="Address", max_length=500, null=False)
    project = models.CharField(verbose_name='Project Code', max_length=50, null=False, unique=True)
    photo = models.ImageField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}& {self.project}"

    # Override the save method to generate a custom primary key
    def save(self, *args, **kwargs):
        # Capitalize the first letter of first_name
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.project = self.project.capitalize()

        # Generate the custom primary key
        self.project = f"{self.project}_{self.first_name}"

        # Call the original save method
        super().save(*args, **kwargs)


class CustomerDetails(models.Model):

    project_names = Customer.objects.values_list('project', flat=True).distinct()
    project_choice = tuple(list([(i, i) for i in project_names]))

    customer = models.ForeignKey(Customer, choices=project_choice, on_delete=models.CASCADE)
    # project_code = models.CharField(choices=project_choice, null=False, max_length=200)
    cust_name = models.CharField(null=False, max_length=200)


