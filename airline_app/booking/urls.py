from django.urls import path

from . import views
app_name = 'booking'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up',views.sign_Up, name ='sign_Up'),
    path('userSettings/<str:userEmail>',views.userSettings,name='userSettings'),

]
