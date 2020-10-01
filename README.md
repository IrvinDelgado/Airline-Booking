# Airline-Booking
Web application created with Django using PostgresSQL

##  Installing
I included pipfiles to run in a virtual environment
Drag this repo into a django project   
In settings.py include
```
CRISPY_TEMPLATE_PACK = 'bootstrap4'
INSTALLED_APPS = [
  'booking.apps.BookingConfig',
  'crispy_forms',
]
```          
In urls.py include it within the urlpatters :  
As well as making sure that `include` is imported from `django.urls`
  
```
path('booking/',include('booking.urls')),
```
