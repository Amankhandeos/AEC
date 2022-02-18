from django.shortcuts import render,redirect
from datetime import datetime
from jobs.models import Orderdetail,User,Product_detail
from jobs.forms import MyForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

#@login_required()
def order_detail(request):
  #if request.user.is_anonymous:
  #      return redirect("/login")

  context = request.session.get('username')

  if request.method=="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          address = request.POST.get('address')
          pin=request.POST.get('pin')
          state=request.POST.get('state')
          radio=request.POST.get('radio')
         # customer=request.session.get('username')
          customer=request.POST.get('user')
          id = request.session.get('product_id')
          Quantity = request.session.get('quantity')
          print(customer)


          order_detail = Orderdetail(product_id=id, quantity=Quantity, name=name, email=email, phone=phone,
                                     address=address, pin=pin, radio=radio, state=state, username=customer,
                                     date=datetime.today())



          b = request.POST.get('radio')
          print(b)
          if b == 'Online Payment':
              return render(request, "Paynow.html")

          if 'bannedmodal' in request.POST:
              form = MyForm(request.POST)
              if form.is_valid():
                  messages.success(request, "Your Order is Success!")
                  order_detail.save()
              else:
                  messages.error(request, "wrong Captcha")


          #else:
           #   return render(request,'CashOnDelivery.html')

  form = MyForm()
  return render(request, "cust_detail.html",{'session':context,'form':form})






