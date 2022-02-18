from jobs.forms import MyForm
from django.contrib import messages
from django.shortcuts import redirect,render

def checkout(request):
    if request.method=="POST":
        form = MyForm(request.POST)
        print(form)
        if form.is_valid():
            messages.success(request, "Your Order is Success!")
        else:
            messages.error(request, "wrong Captcha")

    form = MyForm()

    return render(request,'cust_detail.html',{'form': form})

