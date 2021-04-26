from django.contrib import admin
from .models import Product # relative import as both model.py and models.py on same dir

# Register your models here.
admin.site.register(Product)

