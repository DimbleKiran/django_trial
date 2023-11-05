from django.urls import path
from students import views

urlpatterns = [
    path('api/mechanical/', views.StudentRest.as_view()),
    path('api/mechanical/<pk>', views.StudentUpdDel.as_view()),
]
