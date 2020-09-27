from django.contrib import admin
from .models import Product, Company, Ingredient

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Ingredient)