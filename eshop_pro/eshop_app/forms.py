from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Use for Reset Password------------------
from django.contrib.auth.forms import SetPasswordForm



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

# Use for Reset/forget Password------------------

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=254)

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

#Use to create Profile---
from .models import Customer
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','company_name', 'state','address','address2','postal_zip','email_address','phone','order_notes']



<<<<<<< HEAD


=======
>>>>>>> 1f2cbb7 (add payment gateway)
