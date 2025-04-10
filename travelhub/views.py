from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .loginForm import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
import os
#from dotenv import load_dotenv

#load_dotenv()

from .loginForm import LoginForm, RegisterForm
from .models import RegisterModel

# Create your views here.
def weatherForecast(request):
    destination = request.GET.get('destination', '')  # get destination if provided, else empty
    context = {'destination': destination}
    return render(request, "travel/weather.html", context)

def index(request):
    return render(request,"travel/home.html")

def about(request):
    return render(request,"travel/about.html")

def feedback(request):
    if request.user.is_authenticated:
        return render(request,"travel/feedback.html")
    else:
        return redirect('wander:homePage')

# login of the user
def loginApp(request):
    errMsg=None
    if request.user.is_authenticated:
        return redirect('wander:homePage')
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data['userEmail']
            pswd = loginForm.cleaned_data['userPswd']
            superuser = os.getenv("DATABASE_USER")
            superpswd = os.getenv("DATABASE_PASSWORD")
            print(email,pswd,superuser,superpswd,"What is this: ",(email==superuser) and (pswd==superpswd))
            if ((email==superuser) and (pswd==superpswd)):
                user = User.objects.get(username=email, is_superuser=True)
                login(request,user)
                errMsg="Logged In successfully"
                messages.success(request,errMsg)
                return redirect(reverse('admin:index'))
            elif RegisterModel.objects.filter(userEmail=email,userPswd=pswd).exists():
                regUser = RegisterModel.objects.get(userEmail=email,userPswd=pswd)

                #create an authentication token
                user,created = User.objects.get_or_create(username=regUser.userEmail) #email=username
                print(user)
                if created:
                    user.set_password(regUser.userPswd)
                    user.save() #save it in login authentication token
                login(request,user)
                errMsg="Logged In successfully"
                return redirect('wander:homePage')
            else:
                errMsg="User Not found, Please authenticate yourself by filling registration form"
                messages.error(request,errMsg)
                return redirect('wander:registerPage')
    else:
        loginForm = LoginForm()
    return render(request, "travel/login.html", {"loginDetails": loginForm, "errMsg": errMsg})

# registration of the user
def registerApp(request):
    errMsg=None
    if request.user.is_authenticated:
        return redirect('wander:homePage')
    if request.method=="POST":
        registerForm = RegisterForm(request.POST)
        print("why?",registerForm.is_valid())
        if registerForm.is_valid():
            email = registerForm.cleaned_data.get('userEmail')
            if RegisterModel.objects.filter(userEmail=email).exists():
                errMsg="Email Already Exists! Please use another one"
                messages.error(request,errMsg)
            else:
                registerForm.save()
                errMsg="Account created! Please Login in"
                messages.error(request,errMsg)
                return redirect('wander:loginPage')
    else:
        registerForm = RegisterForm()
    return render(request,"travel/register.html",{
        "registerDetails":registerForm,
        "errMsg":errMsg
    })

def logoutApp(request):
    logout(request)
    return redirect('wander:homePage')