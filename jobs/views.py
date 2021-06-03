from django.shortcuts import render,redirect,HttpResponse #httpresponse is only used to return strings in your webpage
from datetime import datetime    #render is used to return templete.
from jobs.models import Contact,Order_detail
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User,auth
from django.contrib import messages
import razorpay

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context={"variable1" : "this is my first page",
             "variable2" : "startup"
    }
    return render(request,'index.html',context)
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'about.html')
    #return HttpResponse("information about my website")
def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        des=request.POST.get('des')

        if len(name)<3 or len(email)<6 or len(phone)<10 or len(des)<5 :
            messages.error(request,"please enter correct details")
        else:
            contact=Contact(name=name,email=email,phone=phone,des=des,date=datetime.today())
            contact.save()
            messages.success(request,'Your complain has been sent')
    return render(request,'contact.html')
   # return HttpResponse("contact details")
def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'services.html')
    #return HttpResponse("i am ready to serve you"

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
        #check if user has entered correct credentials

    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confpassword = request.POST['password2']

        if password==confpassword:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email):
                messages.success(request, 'Username or Email exists enter other')
                print("Username taken")
                return redirect('/register')


            user=User.objects.create_user(username=username,first_name=first_name,last_name=lastname,email=email,password=password,)
            user.save()

            print("user created")
            messages.success(request, "successfully registered")

        else:
            print("password not matched")
           # messages.success(request, "password not matched")
            return render(request,'register.html')

        return redirect("/login")
    return render(request,'register.html')

def labour(request):
    return render(request,"labour.html")

def payment1(request):

    if request.method=='POST':
        amount = 50000
        order_currency = 'INR'
        client=razorpay.Client(auth={'rzp_test_zetAEowGnXXHd7','l3pQk7TRa1Uzbpu1ulJiKUui'})

        payment=client.order.create({'amount':'amount','currency':'INR','payment_capture':'1'})
        order_receipt = 'order_rcptid_11'
        notes = {
            'Shipping address': 'Bommanahalli, Bangalore'}  # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    return render(request, 'payment1.html')

def order_detail(request):
  if request.method=="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          address = request.POST.get('address')
          pin=request.POST.get('pin')
          state=request.POST.get('state')
          radio=request.POST.get('radio')
          order_detail = Order_detail(name=name, email=email, phone=phone, address=address, pin=pin,radio=radio,state=state,
                                        date=datetime.today())
          order_detail.save()

  return render(request, "cust_detail.html")





