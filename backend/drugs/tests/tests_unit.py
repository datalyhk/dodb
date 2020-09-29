import json
from mixer.backend.django import mixer
from graphene_django.utils.testing import GraphQLTestCase

#from drugs.models import Product, Company, Ingredient
from drugs.schema import schema

PRODUCTS_QUERY = '''
{
  allProducts {
    id
    name
    company {
      id
      name
      address
    }
    ingredients {
      id
      name
    }
    tags
    dateCreated
    lastUpdated
    isActive
  }
}
'''

COMPANIES_QUERY = '''
{
  allCompanies {
    id
    name
    address
    dateCreated
    lastUpdated
    isActive
  }
}
'''

INGREDIENTS_QUERY = '''
{
  allIngredients {
    id
    name
    products {
      id
      name
    }
  }
}
'''
class ProductUnitTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    
    def setUp(self):
        self.product1 = mixer.blend('drugs.Product')
        self.product2 = mixer.blend('drugs.Product')

    def test_all_products_response(self):
        response = self.query(
            PRODUCTS_QUERY,
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        assert len(content['data']['allProducts']) == 2

    def test_product_response(self):
        response = self.query(
          '''
          query product($id: Int!){
            product(id: $id) {
              id
              name
              company {
                name
              }
              ingredients {
                name
              }
              tags
              dateCreated
              lastUpdated
              isActive
            }
          }
          ''',
          variables={'id': 1}
        )

class CompanyUnitTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    
    def setUp(self):
        self.company1 = mixer.blend('drugs.Company')
        self.company2 = mixer.blend('drugs.Company')

    def test_all_companies_response(self):
        response = self.query(
            COMPANIES_QUERY,
        )
        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        assert len(content['data']['allCompanies']) == 2

    def test_company_response(self):
        response = self.query(
          '''
          query company($id: Int!){
            company(id: $id) {
              id
              name
              address
              dateCreated
              lastUpdated
              isActive
            }
          }
          ''',
          variables={'id': 1}
        )

class IngredientUnitTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    
    def setUp(self):
        self.ingredient1 = mixer.blend('drugs.Ingredient')
        self.ingredient2 = mixer.blend('drugs.Ingredient')

    def test_all_ingredients_response(self):
        response = self.query(
            INGREDIENTS_QUERY,
        )

        content = json.loads(response.content)
        print(content)

        self.assertResponseNoErrors(response)
        assert len(content['data']['allIngredients']) == 2

    def test_ingredient_response(self):
        response = self.query(
          '''
          query ingredient($id: Int!){
            ingredient(id: $id) {
              id
              name
              products {
                name
              }
            }
          }
          ''',
          variables={'id': 1}
        )