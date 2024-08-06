from django.contrib import admin
from django.urls import path,include
from .import views


app_name = "eshop_app"

urlpatterns = [
      path("",views.index,name="index"),
      path("shop/",views.shop,name="shop"),
      path("about/",views.about,name="about"),
      path("services/",views.services,name="services"),
      path("blog/",views.blog,name="blog"),
      path("contact/",views.contact,name="contact"),
      path("cart/",views.cart,name="cart"),
      path("checkout/",views.checkout,name="checkout"),
      path("thankyou/",views.thankyou,name="thankyou"),
      
      
      #authentication url -------
        path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
     
]