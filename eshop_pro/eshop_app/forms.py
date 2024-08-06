from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)










#how to use authentication----
# 1 . Create forms.py this page,  
# 2 . move to views.py and import --create templates/register.html and login.html
# 3 . inside app/urls.py, create url 
# 4 . write in setting.py--
# LOGIN_URL = 'eshop_app:login'
# LOGOUT_REDIRECT_URL = 'eshop_app:login' 

# write some things in base.html like 
'''
{% if user.is_authenticated %}
                        <li class="nav-item"><a class="nav-link" href="{% url 'eshop_app:logout' %}">Logout</a></li>
                    {% else %}
                        <li class="nav-item"><a class="nav-link" href="{% url 'eshop_app:login' %}">Login</a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'eshop_app:register' %}">Register</a></li>
                    {% endif %}


'''