from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginuser,name='login'),
    #here the empty quotes represent the default path of the server index that is 127.0.0.1.8000
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),

    path('logout',views.logoutuser,name='logout'),
    path('register',views.register,name='register'),
    path('labour',views.labour,name='labour'),
    path('payment1',views.payment1,name='payment1'),
    path('cust_detail',views.order_detail,name='customer_detail')
]