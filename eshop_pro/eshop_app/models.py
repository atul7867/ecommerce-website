from django.db import models

# Use for shop.html Product related model
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MaxValueValidator

# Create your models here.
class FeedbackForm(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        # return f"{self.fname} and last name is {self.lname}"
<<<<<<< HEAD
        return f'{self.fname}{self.lname}'
=======
        return f'{self.fname}{self.lname}'
    
    # Use for shop.html Product related model-----------------------
    
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman & Diu', 'Daman & Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)

class Customer(models.Model):                          # it will making many to one relation 
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100, default='Default Name')  # For c_fname
    last_name = models.CharField(max_length=100, default='Default Name')  # For c_fname
    company_name = models.CharField(max_length=200, blank=True)  # For Company Name
    state=models.CharField(choices=STATE_CHOICES,max_length=50)
    address = models.CharField(max_length=200, default='Default Name')  # For Address
    address2 = models.CharField(max_length=200, blank=True, default='Default Name')  # For Apartment, suite, unit etc.
    postal_zip = models.CharField(max_length=20, default='Default Name')  # For Postal / Zip Code
    email_address = models.EmailField(default='Default Name')  # For Email Address

    phone = models.CharField(max_length=20, default='Default Name')  # For Phone
    order_notes = models.TextField(blank=True, default='Default Name')  # For Order Notes
    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('C','Chair'),
    ('S','Sofa'),
    ('T','Table'),
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='producting')   # when we are upload images on Admin panel(DB), so automatically create producting folder here
    
    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    



>>>>>>> 1f2cbb7 (add payment gateway)
