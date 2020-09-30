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
            customer = Customer.objects.get(email=userEmailObj)
            payment = PaymentOptions(email = customer)
            payment.save()
            return HttpResponseRedirect(f'/booking/userSettings/{userEmailObj}')
    else:
        form = Sign_Up_Form()
    context = {
        'form':form,
    }
    return render(request, 'booking/sign_up.html',context)

def userSettings(request,userEmail):
    context = {
        'email':userEmail,
    }
    return render(request, 'booking/userSettings.html',context)


def addAddress(request,userEmail):
    user_Payment_Object = PaymentOptions.objects.get(email=userEmail)
    user_item_list = []
    for a in AddressTable.objects.filter(payment_id=user_Payment_Object.payment_id):
        user_item_list.append([a.address,a.address_id])

    if request.method == 'POST':
        form = Add_Address_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/booking/userSettings/{userEmail}/addAddress')
    else:
        form = Add_Address_Form(initial={'payment':user_Payment_Object,})
        form.fields['payment'].widget = forms.HiddenInput()

    context = {
        'form':form,
        'email':userEmail,
        'item_changing':'Address',
        'user_item_list':user_item_list,
    }
    return render(request, 'booking/modifyItem.html',context)

def deleteAddress(request,userEmail,userAddress):
    AddressTable.objects.get(address_id = userAddress).delete()
    return HttpResponseRedirect(f'/booking/userSettings/{userEmail}/addAddress')

def addCreditCard(request,userEmail):
    user_Payment_Object = PaymentOptions.objects.get(email=userEmail)
    user_item_list = []
    for c in CreditCardTable.objects.filter(payment_id=user_Payment_Object.payment_id):
        user_item_list.append([c.credit_card,c.card_id])

    if request.method == 'POST':
        form = Add_CreditCard_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/booking/userSettings/{userEmail}/addCreditCard')
    else:
        form = Add_CreditCard_Form(initial={'payment':user_Payment_Object,})
        form.fields['payment'].widget = forms.HiddenInput()

    context = {
        'form':form,
        'email':userEmail,
        'item_changing':'CreditCard',
        'user_item_list':user_item_list,
    }
    return render(request, 'booking/modifyItem.html',context)

def deleteCreditCard(request,userEmail,userCreditCard):
    CreditCardTable.objects.get(card_id = userCreditCard).delete()
    return HttpResponseRedirect(f'/booking/userSettings/{userEmail}/addCreditCard')

def configureBilling(request,userEmail):
    user_Payment_Object = PaymentOptions.objects.get(email=userEmail)
    user_item_list = []
    for b in BillingInfo.objects.filter(payment_id=user_Payment_Object.payment_id):
        user_Credit_Card_ID = b.credit_card_id
        user_Address_ID = b.address_id
        user_Address = AddressTable.objects.get(address_id=user_Address_ID).address
        user_Credit_Card = CreditCardTable.objects.get(card_id = user_Credit_Card_ID).credit_card
        user_item_list.append([user_Credit_Card,user_Address,b.billing_id])

    if request.method == 'POST':
        form = Billing_Config(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/booking/userSettings/{userEmail}/configureBilling')
    else:
        form = Billing_Config(initial={'payment':user_Payment_Object,})
        form.fields['payment'].widget = forms.HiddenInput()
    context = {
        'form':form,
        'email':userEmail,
        'user_item_list':user_item_list,
    }
    return render(request,'booking/configureBilling.html',context)

def deleteBilling(request,userEmail,billing_id):
    BillingInfo.objects.get(billing_id=billing_id).delete()
    return HttpResponseRedirect(f'/booking/userSettings/{userEmail}/configureBilling')

def store(request,userEmail):
    context = {
        'email':userEmail,
    }
    return render(request,'booking/store.html',context)