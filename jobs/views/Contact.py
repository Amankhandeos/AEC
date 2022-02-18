from django.shortcuts import render,redirect
from datetime import datetime
from jobs.models import Contact
#from jobs.middlewares.auth import auth_middleware
#from django.utils.decorators import method_decorator

#@method_decorator(auth_middleware)
def contact(request):
    #if request.user.is_anonymous:
     #   return redirect("/login")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        des=request.POST.get('des')
        message=None
        value={'name':name,
               'email':email,
               'phone':phone}
        contact = Contact(name=name, email=email, phone=phone, des=des, date=datetime.today())

        if len(email)<6:
            message="Email is invalid !!"
        elif len(phone)<5:
            message="Phone number is invalid !!"
        elif len(des)<10:
            message="Description is too short !!"

        if not message:
            contact.save()
            message = "Your complain has been sent"
            return render(request, 'contact.html',{'error':message})

        else:
            data={'error':message,
                  'value':value}

            return render(request,'contact.html',data)
    return render(request,'contact.html')
