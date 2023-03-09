from random import randrange
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from datetime import datetime
from zoneinfo import ZoneInfo


#username:- admin and pass::- admin

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect("/sign_in")
    

# <------------------Autintication sign in sign up class start here------------------------------>


class Auth:
      # <---------------------------Signin  Function is start here------------------------------>
    def sign_in(request):
        if request.method =="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate( request,username=username, password=password)
            # check if user entered correct crediantials
            if user is not None:
                login(request, user)
                #send Signal 1 to indicate login succesfully
                return HttpResponse("1")
                # return redirect("/")
                # A backend authenticated the credentials
            else:
                # No backend authenticated the credentials
                #send Signal 0 to indicate Something went Wrong
                return HttpResponse("0")
        else:
            return render(request,"sign_in.html")

        # <------------------Signup function is start here------------------------------>

    def sign_up(request):
        # cHECK FOR pOST method and get the All required field
        if request.method =='POST':
            fname = request.POST.get('fname')
            password = request.POST.get('password')
            username = request.POST.get('username')
            email = request.POST.get('email')
            print(fname,password,username,email)
            User.objects.create_user(email=email,username=username, password=password,first_name=fname).save()
            return HttpResponse(1)
        return render(request,"sign_up.html")

    # <------------------Logout/Sign-out  function is start here------------------------------>

    def sign_out(request):
        logout(request)
        return redirect("/")
        



