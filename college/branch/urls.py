from django.urls import path
from branch import views

urlpatterns = [
    path('mechanical/', views.Mechanical_forms),
    path('update/<id>/', views.update),
    path('delete/<id>/', views.delete),

]
