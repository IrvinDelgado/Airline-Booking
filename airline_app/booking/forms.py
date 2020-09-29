from django import forms
from django.forms import ModelForm
from .models import *

class Sign_In_Form(ModelForm):
    class Meta:
        model = Customer
        fields = ['email','name']

    name = forms.CharField(required=True)
    
    def clean(self):
        email = self.cleaned_data.get("email")
        name = self.cleaned_data.get("name")

        if email and name:
            try:             
                matchEmail = Customer.objects.get(email=email,name=name)         
            except Customer.DoesNotExist:             
                raise forms.ValidationError("email or username don't match")  

class Sign_Up_Form(ModelForm):
    class Meta:
        model = Customer
        fields = ['email','name','iata']
    name = forms.CharField(required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')


