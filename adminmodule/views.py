from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Info
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth
from .models import Info

# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html ')

def generalhomepage(request):
    return render(request,'generalhomepage.html')

def userhomepage(request):
    return render(request,'userhomepage.html')
def Login(request):
    return render(request,'adminmodules/Login.html')

def Signup(request):
    return render(request,'adminmodules/Signup.html')

def signup1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'adminmodules/Signup.html')

        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.save()

        # Redirect to the login page
        return redirect('Login')  # Assuming 'Login' is the correct URL name for your login page

    return render(request, "adminmodules/Signup.html")

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            # Redirect to the userhomepage after successful login
            return redirect('/userhomepage')  # Change 'userhomepage' to the appropriate URL name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'adminmodules/Login.html')














