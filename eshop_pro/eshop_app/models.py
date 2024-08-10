from django.db import models

# Create your models here.
class FeedbackForm(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        # return f"{self.fname} and last name is {self.lname}"
        return f'{self.fname}{self.lname}'