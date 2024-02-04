from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()


def login_view(request):
    if request.method == 'POST': 
        print('hi')   
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.user = authenticate(request, username= username, password= password)
        if request.user:
            login(request, request.user)
            messages.info(request, "success", extra_tags='success')
            return redirect("Home")
    print("hi2")
    return render(request, 'Accounts/login.html')




def logout_view(request):
    logout(request)
    return redirect('Home')