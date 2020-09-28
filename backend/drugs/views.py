from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Product, Company, Ingredient
from django.http import Http404
from rest_framework import status

class Products(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):

    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data)

class Companies(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = serializers.CompanySerializer(companies, many=True)
        return Response(serializer.data)

class CompanyDetail(APIView):

    def get(self, request, product_id):
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise Http404
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data)

class Ingredients(APIView):

    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = serializers.IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

class IngredientDetail(APIView):

    def get(self, request, ingredient_id):
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist:
            raise Http404
        serializer = serializers.IngredientSerializer(ingredient)
        return Response(serializer.data)