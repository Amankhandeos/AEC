import razorpay
from django.shortcuts import render,redirect
#from django.contrib.auth.decorators import login_required
from jobs.models import Product_detail
from django.views import View

#@login_required()

def payment1(request,pk=None):
    if request.method=="GET":
        product = Product_detail.objects.get(pk=pk)
        print(product)
        request.session['product_id'] = product.id
        profuct=request.session.get('product_id')
        print(profuct)
        worker = Product_detail.objects.filter(category=product.category)
        return render(request, 'payment1.html', {'product': product, 'labour': worker})

    elif request.method=="POST":
        quantity=request.POST.get('quantity')

       # Product_id=product_id.product_id

        request.session['quantity']=quantity

        Quantity=request.session.get('quantity')
        print(Quantity)

        return redirect('/cust_detail')





