from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings
import random

# Use for Reset Password------------------
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from .forms import PasswordResetRequestForm, SetPasswordForm

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

otp_storage = {}

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            otp = random.randint(100000, 999999)
            otp_storage[email] = otp
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            request.session['registration_data'] = form.cleaned_data
            messages.success(request, 'OTP sent to your email.')
            return redirect('eshop_app:verify_otp')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'hide_header_and_footer': True})

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        if otp_storage.get(email) == int(otp):
            registration_data = request.session.get('registration_data')
            if registration_data:
                form = CustomUserCreationForm(registration_data)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    messages.success(request, 'Registration successful.')
                    return redirect('eshop_app:login')
                else:
                    messages.error(request, 'Form data is not valid.')
            else:
                messages.error(request, 'Registration data not found in session.')
            del otp_storage[email]
        else:
            messages.error(request, 'Invalid OTP.')
    return render(request, 'verify_otp.html',{'hide_header_and_footer': True})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('eshop_app:index')  # Redirect to a home page or dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form, 'hide_header_and_footer': True})

def user_logout(request):
    logout(request)
    return redirect('eshop_app:login')

#use for resend otp on the  manully (verify_otp.html) template------------
def request_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = random.randint(100000, 999999)
        otp_storage[email] = otp
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        messages.success(request, 'OTP sent to your email.')
        return redirect('eshop_app:verify_otp')
    return render(request, 'request_otp.html',{'hide_header_and_footer':True})



def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': get_current_site(request).domain,
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
            return redirect("eshop_app:password_reset_done")
    form = PasswordResetRequestForm()
    return render(request, "password_reset_form.html", {"form": form,'hide_header_and_footer':True})

def password_reset_done(request):
    return render(request, "password_reset_done.html",{'hide_header_and_footer':True})


def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user=user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been set. You can now log in.')
                return redirect('eshop_app:password_reset_complete')
        else:
            form = SetPasswordForm(user=user)
    else:
        messages.error(request, 'The reset link is no longer valid.')
        return redirect('eshop_app:password_reset')

    return render(request, 'password_reset_confirm.html', {'form': form,'hide_header_and_footer':True})

def password_reset_complete(request):
    return render(request, "password_reset_complete.html",{'hide_header_and_footer':True})








# Second method for authentation(Without creating forms.py)-------------------------------


# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# from django.db import IntegrityError
# from django.contrib import messages

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         password_confirm = request.POST.get('password_confirm')
#         email = request.POST.get('email')

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             return render(request, 'register.html', {'error': 'Username already exists', 'hide_header_and_footer': True})

#         # Check if passwords match
#         if password != password_confirm:
#             return render(request, 'register.html', {'error': 'Passwords do not match', 'hide_header_and_footer': True})

#         try:
#             # Create and save user
#             user = User.objects.create_user(username=username, email=email)
#             user.set_password(password)
#             user.save()

#             # Send confirmation email
#             subject = 'Account Creation Confirmation'
#             message = f'Hello {username},\n\nYour account has been successfully created.'
#             from_email = settings.EMAIL_HOST_USER
#             to_email = [email]
#             send_mail(subject, message, from_email, to_email)

#             return redirect('eshop_app:login')
#         except IntegrityError:
#             return render(request, 'register.html', {'error': 'Failed to create user', 'hide_header_and_footer': True})
#     else:
#         return render(request, 'register.html', {'hide_header_and_footer': True})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('eshop_app:index')
#         else:
#             messages.error(request, 'Invalid username or password')

#     return render(request, 'login.html', {'hide_header_and_footer': True})

# def user_logout(request):
#     logout(request)
#     return redirect('eshop_app:login')
