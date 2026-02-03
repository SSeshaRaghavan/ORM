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