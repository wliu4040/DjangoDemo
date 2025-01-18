from django.db import models

# Create your models here. inheriting from models.Model
# This will map tot he database
class Product(models.Model):
    title       = models.CharField(max_length = 120) # max_length = required
    description = models.TextField(blank = True, null = True) # Blank has to deal with whether it's required when rendered
    price       = models.DecimalField(decimal_places = 2, max_digits = 1000)
    summary     = models.TextField(blank = False, null = False) # Null has to deal with whether it can be empty in database
    featured    = models.BooleanField() # null = True, default = True