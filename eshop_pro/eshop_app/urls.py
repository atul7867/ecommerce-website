from django.contrib import admin
from django.urls import path,include
from .import views

from django.contrib.auth import views as auth_views

# Use for show address on contact page 
# from .views import get_address
<<<<<<< HEAD
=======

>>>>>>> 1f2cbb7 (add payment gateway)

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
    path('verify_otp/', views.verify_otp, name='verify_otp'),
         path('request-otp/', views.request_otp, name='request_otp'),
  
  
  # Use for Reset Password------------------

      path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
     
    # Use for show address on contact page 
    # path('api/get-address/', get_address, name='get_address'),
    
    
    path('feedback_form/', views.feedback_form, name='feedback_form'),
<<<<<<< HEAD

=======
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product_details/',views.product_view,name="product_details"),
    path('profile/',views.profile,name="profile"),
    path('profile_view/',views.profile_view,name="profile_view"),
    path('placeorder/',views.placeorder,name="placeorder"),
    
      
>>>>>>> 1f2cbb7 (add payment gateway)
]