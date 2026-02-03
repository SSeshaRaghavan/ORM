# Ex02 Django ORM Web Application
# Date:
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM
models.py
```
from django.db import models
from django.contrib import admin
# Create your models here.
class product(models.Model):
    Name=models.CharField(max_length=100)
    product_id=models.IntegerField(primary_key=True)
    Brand=models.CharField(max_length=20)
    Price=models.FloatField()
    Manufracture_date=models.DateField()
    Expiry_date=models.DateField()
    Warrenty=models.CharField(max_length=10)
class ProductAdmin(admin.ModelAdmin):
    list_display=['Name','product_id','Brand','Price','Manufracture_date','Expiry_date','Warrenty']
```
admin.py
```
from django.contrib import admin
from .models import product,ProductAdmin
# Register your models here.
admin.site.register(product,ProductAdmin)
```
# OUTPUT
Include the screenshot of your admin page.
![alt text](<Screenshot 2026-02-03 104102.png>)
# RESULT
Thus the program for creating a database using ORM hass been executed successfully
