from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Sign_In_Form(request.POST)
        if form.is_valid():
            userEmailObj = request.POST.get('email',None)
            user = Customer.objects.get(email = userEmailObj)
            return HttpResponseRedirect(f'/booking/userSettings/{user.email}')
    else:
        form = Sign_In_Form()
    context = {
        'form':form,
    }
    return render(request, 'booking/index.html',context)

