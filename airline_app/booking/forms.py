from django import forms
from django.forms import ModelForm
from .models import *

class Sign_In_Form(ModelForm):
    class Meta:
        model = Customer
        fields = ['email','name']

    name = forms.CharField(required = True)

    def clean_email(self):         
        email = self.cleaned_data.get('email')         
        try:             
            matchEmail = Customer.objects.get(email=email)         
        except Customer.DoesNotExist:             
            raise forms.ValidationError('This email does not exist!')         
        return self.cleaned_data.get('email')      
    
    def clean_name(self):         
        name = self.cleaned_data.get('name')         
        try:             
            matchName = Customer.objects.get(name=name)         
        except Customer.DoesNotExist:             
            raise forms.ValidationError("This name either doesn't match email or doesn't exist")         
        return name



