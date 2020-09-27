from django.db import models

class Product(models.Model):
    """
    Stores list of products/drugs registered in offical drug office database
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    # name: Product Name
    reg_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    # reg_no: equivalent to "permit_no" in drug database
    ingredients = models.ManyToManyField('Ingredient', related_name='products')
    # Company Name and Company Address
    company = models.ForeignKey(
        'Company', on_delete=models.PROTECT,
        )
    tags = models.CharField(max_length=255,blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['reg_no']
  
    def __str__(self):
        return f"{self.reg_no} | {self.name}"

class Company(models.Model):
    """
    Stores list of company names and addresses in official drug office database
    """
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_certholder = models.BooleanField(default=True)
    # is_certholder: Companies imported from drug database are certificate holders 
    is_supplier = models.BooleanField(default=False)
    # is_supplier: Companies may also be a supplier
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated  = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """
    Stores list of ingredients
    """
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

