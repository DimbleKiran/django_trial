from django.contrib import admin
from django.urls import path
from branch import views

urlpatterns = [
    path('admins/', views.data),
]
