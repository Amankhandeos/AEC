from django.shortcuts import render,redirect
def services(request):
    #if request.user.is_anonymous:
     #   return redirect("/login")
    return render(request,'services.html')