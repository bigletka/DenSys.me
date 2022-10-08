import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import UserCreateForm

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = get_user_model().objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR Password does not exist")

    context = {}
    return render(request, 'login_page.html', context)





def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreateForm()
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = get_user_model().objects.create_user(email=email, password=password)
            return redirect('home')
    return render(request, 'register.html', {'form':form})  



def home(request):
    return render(request,'home.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')

def make_an_appointment(request):
    return render(request, 'make_an_appointment.html')

def about_us(request):
    return render(request, 'about_us.html')
