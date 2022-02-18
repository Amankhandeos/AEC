from django.shortcuts import render,redirect
def about(request):
   # if request.user.is_anonymous:
    #    return redirect("/login")
    return render(request,'about.html')