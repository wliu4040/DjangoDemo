from django.contrib import admin

#.models makes it a relative import. Imports product class from models.py
from .models import Product
# Register your models here.

admin.site.register(Product)