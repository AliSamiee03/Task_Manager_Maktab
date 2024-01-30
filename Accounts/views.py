from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username= username, password= password)
            if user:
                login(request, user)
                return redirect('Home')


    else:
        form = LoginForm()

    content = {'form': form}

    return render(request, 'Accounts/login.html', content)

def logout_view(request):
    logout(request)
    return redirect('Home')