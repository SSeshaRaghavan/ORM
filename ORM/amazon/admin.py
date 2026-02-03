from django.contrib import admin
from .models import product,ProductAdmin
# Register your models here.
admin.site.register(product,ProductAdmin)