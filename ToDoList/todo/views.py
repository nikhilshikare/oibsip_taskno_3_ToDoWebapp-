from random import randrange
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from todo.models import TODO
from datetime import datetime
from zoneinfo import ZoneInfo


#username:- admin and pass::- admin

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        completed_todo=TODO.objects.all().filter(username=request.user.username,is_completed=True)
        uncompleted_todo=TODO.objects.all().filter(username=request.user.username,is_completed=False)
        context={
            'status':-1,
            'completed_todo':completed_todo,
            'uncompleted_todo':uncompleted_todo
            }
        return render(request,'home.html',context=context)
    else:
        return redirect("/sign_in")


    
class TODO_LIST:
      # <---------------------------Add To Do Start Here------------------------------>
    def add_todo(request):
        if request.method =="POST":
            desc = request.POST.get("desc")
            title = request.POST.get("title")
            dateobj = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')
            TODO(title=title,desc=desc,username=request.user.username,time=dateobj).save()
            context={'status':1}
            # check if user entered correct crediantials
            return render(request,"home.html",context=context)
        else:
            context={'status':0}
            return render(request,"home.html",context=context)
        
    def delete_id(request):
        id = request.GET.get("id")
        try:  
            TODO.objects.filter(id=id).delete()
            context={'status':1}
        except:
            context={'status':0}
        # check if user entered correct crediantials
        return render(request,"home.html",context=context)
    
    def add_complete(request):
        id = request.GET.get("id")
        try:  
            dateobj = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')
            TODO.objects.filter(id=id).update(is_completed=True,completed_time=dateobj)
            context={'status':1}
        except:
            context={'status':0}
        # check if user entered correct crediantials
        return render(request,"home.html",context=context)
    
    def edit_todo(request):
        if request.method =="POST":
            desc = request.POST.get("desc")
            title = request.POST.get("title")
            id = request.POST.get("todo_id")
            try:  
                TODO.objects.filter(id=id).update(id=id,desc=desc,title=title)
                return HttpResponse('1')
            except:
                return HttpResponse('0')
            # check if user entered correct crediantials
        else:
            return HttpResponse('-1')


    

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
        



