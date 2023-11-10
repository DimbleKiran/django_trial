"""
URL configuration for trialProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('customerforms/', views.customer_views_forms),
    path('customertables/', views.customer_views_table),
    path('feed/', views.video_feed, name='video_feed'),
    path('delete/<id>/', views.delete),
    path('customerdetails/', views.customer_details_view_form),
    path('customerdetailstables/', views.customer_details_table),

]
