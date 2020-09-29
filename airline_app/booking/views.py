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
            userEmailSubmitted = request.POST.get('email',None)       
            return HttpResponseRedirect(f'/booking/userSettings/{userEmailSubmitted}')
    else:
        form = Sign_In_Form()
    context = {
        'form':form,
    }
    return render(request, 'booking/index.html',context)

def sign_Up(request):
    if request.method == 'POST':
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
            userEmailObj = request.POST.get('email',None)
            return HttpResponseRedirect(f'/booking/userSettings/{userEmailObj}')
    else:
        form = Sign_Up_Form()
    context = {
        'form':form,
    }
    return render(request, 'booking/sign_up.html',context)

def userSettings(request,userEmail):
    return render(request, 'booking/userSettings.html')
