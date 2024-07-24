from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                
                print('User', user)

                print(request.user)
                print(request.user.is_authenticated)

                return redirect('/')

    print("Rendering login template")        
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if name and email and password and password2:
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already taken.')
                else:
                    user = User.objects.create_user(name=name, email=email, password=password)
                    messages.success(request, 'Account created successfully. Please log in.')
                    return redirect('account:login')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'account/signup.html')
