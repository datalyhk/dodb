from graphene_django import DjangoObjectType

from .models import Product, Company, Ingredient

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'reg_no',
            'ingredients',
            'company',
            'tags',
            'date_created',
            'last_updated',
            'is_active',
        )

class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'address',
            'date_created',
            'last_updated',
            'is_active',
        )

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'products',
        )