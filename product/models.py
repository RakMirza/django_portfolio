from django.db import models

# Create your models here
class Product(models.Model):
    # following are the attributes of  class product and mapping to database
    title                = models.CharField(max_length=100)
    description    = models.TextField(blank=True, null = True)
    price              = models.DecimalField(max_digits=5,decimal_places=2)
    summary       = models.TextField(blank=True, null= False)
    featured        = models.BooleanField(default=False)