from django.shortcuts import render
from .forms import SignUp
from django.http import HttpResponseRedirect


def home(r):
    return render(r, "home.html")


def signup(r):
    form1 = SignUp                                                      # forms from forms.py
    if r.method == 'POST':
        forms_s = SignUp(r.POST)                                        # create new forms with new data
        if forms_s.is_valid():
            user = forms_s.save()                                       # save forms in var
            user.set_password(user.password)                            # pass the password to set_password to encrypt
            user.save()
            return HttpResponseRedirect('/')
    return render(r, 'registration/signup.html', {"form1": form1})
