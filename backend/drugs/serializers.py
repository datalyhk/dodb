from .models import Product, Company, Ingredient
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'reg_no', 'ingredients', 'company', 
            'tags', 'last_updated', 'is_active',
            ]
        read_only_fields = fields

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'last_updated', 'is_active',]
        read_only_fields = fields

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'products',]
        read_only_fields = fields