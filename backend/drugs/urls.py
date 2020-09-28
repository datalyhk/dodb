from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Products.as_view()),
    path('products/<str:product_id>/', views.ProductDetail.as_view()),
    path('products/<str:product_id>/ingredients/', views.Ingredients.as_view()),
    path('products/<str:product_id>/ingredients/<str:ingredient_id>', views.IngredientDetail.as_view()),
    path('companies/', views.Companies.as_view()),
    path('companies/<str:company_id>/', views.CompanyDetail.as_view()),
    path('ingredients/', views.Ingredients.as_view()),
    path('ingredients/<str:ingredient_id>/', views.IngredientDetail.as_view()),
]