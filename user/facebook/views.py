from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User
from django.views.decorators.cache import never_cache

# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        name = request.POST["firstname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeat = request.POST["repeat"]
        print(name, email, password, repeat)
        enpassword = make_password(password, salt="123")

        if password != repeat:
            messages.error(request, "Password Mismatched")

        else:
            try:
                print(name, email, password, repeat)
                u1 = User(
                    names=name,
                    emails=email,
                    passwords=password,
                )
                u1.save()
                print(name, email, password, repeat)
                messages.success(request, "User registered")
            except Exception as ex:
                messages.error(request, ex)
        return render(request, "register.html")

    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        

        if User.objects.filter(emails=email, passwords=password).exists():
            messages.success(request, "Valid Login")

            u1=User.objects.get(emails=email,passwords=password)
            u1id=u1.id

            # setting session object because to pass the data in other functions as well or making the variables to public
            request.session['my_email']=email
            request.session['my_uid']=u1id

            return redirect(home)

        else:
            messages.error(request, "Invalid Login")

    return render(request, "login.html")

@never_cache
def home(request):
    if 'my_email' in request.session:
        my_em=request.session['my_email']
        context={'my_em':my_em}
        return render(request,'home.html',context)
    else:
        return redirect('login_page')


def profile(request):
    return render(request,'profile.html')