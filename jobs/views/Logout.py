from django.contrib.auth import logout
from django.shortcuts import render,redirect
def logoutuser(request):
    #if request.user.is_anonymous:
     #   return redirect("/login")
    request.session.clear()
    return redirect("/login")