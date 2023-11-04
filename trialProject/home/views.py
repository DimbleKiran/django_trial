from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def home(r):
    return render(r, 'home.html')
