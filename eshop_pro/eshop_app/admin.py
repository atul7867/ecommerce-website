from django.contrib import admin
<<<<<<< HEAD
from .models import FeedbackForm
# Register your models here.
admin.site.register(FeedbackForm)
=======
from .models import FeedbackForm,Product,Customer,Cart,OrderPlaced
# Register your models here.
admin.site.register(FeedbackForm)


#To display your models in a more professional and readable way on the Django admin panel
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user'  ,'first_name','last_name','company_name', 'state','address','address2','postal_zip','email_address','phone','order_notes')
    search_fields = ('user__username', 'state','email_address')
    list_filter = ('state','phone')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'brand', 'category')
    search_fields = ('title', 'brand', 'category')
    list_filter = ('category', 'brand')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    search_fields = ('user__username', 'product__title')

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status')
    search_fields = ('user__username', 'customer__name', 'product__title')
    list_filter = ('status', 'ordered_date')

# Registering the models with the customized admin classes
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(OrderPlaced, OrderPlacedAdmin)
>>>>>>> 1f2cbb7 (add payment gateway)
