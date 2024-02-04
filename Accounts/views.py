from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            request.user = authenticate(request, username= username, password= password)
            print(f"user : {request.user}")
            if request.user:
                login(request, request.user)
                messages.info(request, "success", extra_tags='success')
                return redirect("Home")
            else:
                messages.error(request, "Unsuccess", extra_tags='error')
                return redirect("login")
            
    else:
        form = LoginForm()

    content = {'form': form}
    return render(request, 'Accounts/login.html', content)

def logout_view(request):
    logout(request)
    return redirect('Home')