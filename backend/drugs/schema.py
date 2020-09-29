import graphene

from .models import Product, Company, Ingredient
from .types import ProductType, CompanyType, IngredientType

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())

    all_companies = graphene.List(CompanyType)
    company = graphene.Field(CompanyType, company_id=graphene.Int())

    all_ingredients = graphene.List(IngredientType)
    ingredient = graphene.Field(IngredientType, ingredient_id=graphene.Int())

    def resolve_all_products(root, info, **kwargs):
        return Product.objects.select_related('company').all()

    def resolve_product(root, info, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None

    def resolve_all_companies(root, info, **kwargs):
        return Company.objects.select_related('product').all()

    def resolve_company(root, info, company_id):
        try:
            return Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            return None

    def resolve_all_ingredients(root, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_ingredient(root, info, ingredient_id):
        try:
            return Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)