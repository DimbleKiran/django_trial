from django.contrib import admin
from django.urls import path, include
from admins import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('branch/', include('branch.urls')),
    path('admins/', include('admins.urls')),
    path('students/', include('students.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.signup),
]
