from django.shortcuts import render, redirect
from jobs.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt,csrf_protect,ensure_csrf_cookie

@csrf_protect
def loginuser(request):
    if request.method == "GET":
        return render(request, "login.html")

    else:

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.get_customer(username, password)
        error_message = None
        if user:
           # flag = check_password(password,user.password)

            request.session['user_id'] = user.id
            request.session['username'] = user.username


            # if password==user.password:
            return redirect('/')

            # else:
            #   error_message = 'Email or Password invalid !!'

        else:
            error_message = 'Email or Password invalid !!'
        # check if user has entered correct credentials

    return render(request, 'login.html', {'error': error_message})
