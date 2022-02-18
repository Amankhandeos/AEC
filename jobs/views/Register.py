from django.shortcuts import render,redirect
from jobs.models import User

def register(request):
   # if request.user.is_anonymous:
    #    return redirect("/login")
    if request.method=='GET':
        return render(request,'register.html')
    else:
        postData=request.POST
        first_name=postData.get('first_name')
        lastname = postData.get('last_name')
        username = postData.get('username')
        email = postData.get('email')
        phone=postData.get('phone')
        password = postData.get('password1')
        confpassword =postData.get('password2')
        error_message=None
        value={
            'first_name' : first_name,
            'last_name' :lastname,
            'username' :username,
            'email' :email,
            'phone' :phone,


        }
        user = User(username=username, first_name=first_name, last_name=lastname, email=email, password=password,
                    phone=phone, )

        if len(username)<4:
            error_message="Username must be more than 4 charter"
        elif password!=confpassword:
            error_message="Password not matched"
        elif len(email)<5:
            error_message="Email is not valid"
        elif len(phone)<5:
            error_message="Phone number is not valid"

        elif user.isExists():
            error_message="username already exits"
       # elif user.objects.filter(username=username):
               # messages.success(request, 'Username or Email exists enter other')

                #return redirect('/register',{'values' :value})
        #elif user.objects.filter(email=email):
         #   error_message="email already exits"

        if not error_message:
            user.save()

            return render(request,'login.html',{'success':'Registered Successfully'})
        else:
            data={
                'error': error_message,
                'value': value,
            }
            #error_message="password not matched"
          #  print("password not matched")
           # messages.success(request, "password not matched")
            return render(request,'register.html',data)
