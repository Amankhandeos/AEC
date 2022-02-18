from django.shortcuts import render,redirect
#from jobs.models import Customer
#from django.contrib.auth.decorators import login_required

#@login_required(login_url='/accounts/login/')
def index(request):
    if request.session.get('username'):
        context = {"variable1": "this is my first page",
                   "variable2": "startup"
                   }
        print('you are :', request.session.get('username'))
        return render(request, 'index.html', context)

    else:
        return redirect('/login')

