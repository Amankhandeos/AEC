from django.urls import path
from .views import About,Contact,home,Labour,Login,Logout,Order_details,Payment,Register,Services,checkout

urlpatterns = [
    path('',home.index,name='index'),
    path('login',Login.loginuser,name='login'),
    #here the empty quotes represent the default path of the server index that is 127.0.0.1.8000
    path('about',About.about,name='about'),
    path('contact',Contact.contact,name='contact'),
    path('services',Services.services,name='services'),

    path('logout',Logout.logoutuser,name='logout'),
    path('register',Register.register,name='register'),
    path('labour/<slug:data>',Labour.labour,name='labour'),
    path('payment1',Payment.payment1,name='payment1'),
    path('payment1/<int:pk>',Payment.payment1,name='payment1'),
    path('cust_detail',Order_details.order_detail,name='customer_detail'),
    path('check-out',checkout.checkout,name='checkout')

]