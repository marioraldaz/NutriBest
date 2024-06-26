from django.urls import path
from .view_ingredient import IngredientView
from .view_recipe import *

urlpatterns = [
    path('ingredient/save/', IngredientView().save_ingredient, name='save_ingredient'),
    path('fetch-filtered-ingredients/', IngredientView().fetch_filtered_ingredients, name="fetch_filtered_ingredients"),
    path('get-ingredient-details/<int:id>/<int:amount>/', IngredientView().get_ingredient_info, name="get_ingredient_details"),
    path('fetch-ingredients-by-name/<str:name>/', IngredientView().fetch_ingredients_by_name, name='fetch_ingredients_by_name'),
    path('recipe/save/', save_recipe, name='save_recipe'),
    path('fetch-filtered-recipes/', fetch_filtered_recipes, name='fetch_filtered_recipes'),
    path('get-recipe-info/<int:id>/',get_recipe_info, name='get_recipe_info'),
    path('fetch-recipes-by-name/<str:name>', fetch_recipes_by_name, name='fetch_recipes_by_name'),
    path('update-nutrition/',update_nutrition_for_recipe, name='modify_recipe')
]

