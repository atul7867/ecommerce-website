from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,"index.html")

def shop(request):
    return render(request,'shop.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
@login_required
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def thankyou(request):
    return render(request,'thankyou.html')


#authenitation-------------------start

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eshop_app:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form,'hide_header_and_footer':True})  # use for 'hide_header_and_footer':True, we want show register.html on blank page without header and footer of base.html


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('eshop_app:index')  # Redirect to a home page or dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form,'hide_header_and_footer':True})

def user_logout(request):
    logout(request)
    return redirect('eshop_app:login')  
