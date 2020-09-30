from django.urls import path

from . import views
app_name = 'booking'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up', views.sign_Up, name ='sign_Up'),
    path('userSettings/<str:userEmail>', views.userSettings, name='userSettings'),
    path('userSettings/<str:userEmail>/addAddress', views.addAddress, name='addAddress'),
    path('userSettings/<str:userEmail>/deleteAddress/<str:userAddress>', views.deleteAddress, name='deleteAddress'),
    path('userSettings/<str:userEmail>/addCreditCard', views.addCreditCard, name='addCreditCard'),
    path('userSettings/<str:userEmail>/deleteCreditCard/<str:userCreditCard>', views.deleteCreditCard, name='deleteCreditCard'),
    path('userSettings/<str:userEmail>/configureBilling', views.configureBilling, name='configureBilling'),
    path('userSettings/<str:userEmail>/configureBilling/deleteBilling/<str:billing_id>', views.deleteBilling, name='deleteBilling'),

]
