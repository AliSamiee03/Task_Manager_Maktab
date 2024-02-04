from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import get_user_model



def login_view(request):
    if request.method == 'POST':    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            messages.info(request, "success", extra_tags='success')
            return redirect("Home")
        else:
            print('error')
            messages.info(request, "error", extra_tags='error')
            return redirect('login')
        
    return render(request, 'Accounts/login.html')


def signup_view(request):

    if request.method == 'POST':    
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = get_user_model().objects.create_user(username=username, password=password, email=email, is_staff=True)
        user.save()
        login(request, user)
        messages.info(request, "success", extra_tags='success-signup')
        return redirect("Home")
    
    return render(request, 'Accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('Home')