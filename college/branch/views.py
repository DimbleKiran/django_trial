from django.shortcuts import render
from .forms import MechForms
from django.http import HttpResponseRedirect, HttpResponse
from .models import Mechanical
from django.contrib.auth.decorators import login_required


# print(forms.cleaned_data)

def Mechanical_forms(r):
    mech_user = MechForms
    if r.method == 'POST':
        forms = MechForms(r.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse('<h1>Successful...</h1>')
    return render(r, 'branch/mechanical.html', {"mech_user": mech_user})


@login_required()
def data(r):
    table = Mechanical.objects.all()
    return render(r, 'admins/admins.html', {"table": table})


def update(r,id):
    obj = Mechanical.objects.get(id=id)                         # fetch data from database for particular id
    if r.method == 'POST':
        form_u = MechForms(r.POST, instance=obj)                # map data from database & data from user
        if form_u.is_valid():
            form_u.save()
            return HttpResponseRedirect('/admins/admins')
    return render(r, 'branch/mech_update.html', {'obj': obj})


def delete(r, id):
    obj = Mechanical.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/admins/admins')

