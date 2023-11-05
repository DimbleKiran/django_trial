from django.contrib import admin
from .models import Mechanical


class MechAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "phone", "email", "gender"]


admin.site.register(Mechanical, MechAdmin)
