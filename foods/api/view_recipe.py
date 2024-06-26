from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..recipe import Recipe
from .recipe_serializer import RecipeSerializer
from ..nutrition import Nutrition
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponseServerError
from rest_framework import status
from .nutrition_serializer import NutritionSerializer

def save_recipe(request):
    try:
        # Deserialize the JSON data from the request body into a Recipe object
        recipe_data = json.loads(request.body)
        serializer = RecipeSerializer(data=recipe_data)
        if serializer.is_valid():
            # Save the validated Recipe object to the database
            serializer.save()
            return Response(serializer.data, status=201)  # Return the serialized Recipe object
        else:
            return Response(serializer.errors, status=400)  # Return validation errors
    except Exception as e:
        return Response({'error': str(e)}, status=500)  # Return any other errors

@api_view(['GET'])
def get_recipe_info(request, id):
    recipe_id = id
    # Check if a recipe with the same spoonacular_id already exists
    existing_recipe = Recipe.objects.filter(spoonacular_id=recipe_id).first()
    
    if existing_recipe:
        # If the recipe exists, serialize it and return it
        serialized_recipe = RecipeSerializer(existing_recipe).data
        nutrition = NutritionSerializer(existing_recipe.nutrition).data
        
        serialized_recipe['nutrition'] = nutrition

        return Response(serialized_recipe, status=status.HTTP_200_OK)

    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?includeNutrition=true'
    params = {
        'apiKey': settings.API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for any error status codes
        data = response.json()

        # Extract necessary data from Spoonacular API response
        nutrition_data = data.get('nutrition', {})
        ingredients_data = data.get('extendedIngredients', [])
        # Create Nutrition object
        nutrition = Nutrition.create_from_json(nutrition_data)
                # Iterate over the list of ingredient objects
        for ingredient in ingredients_data:
            ingredient_id = ingredient.get('id')  # Extract the ID from the ingredient object
            if ingredient_id:
                ingredient_url = f'http://localhost:8000/api/get-ingredient-details/{ingredient_id}/1/'
                # Call the function to get recipe info based on the ingredient ID
                ingredientFetched =  requests.get(ingredient_url)
                print(ingredientFetched)
                if ingredientFetched:
                    # Process the recipe data as needed
                    print(f"Recipe info for ingredient ID {ingredient_id}: {ingredientFetched}")
                else:
                    print(f"Failed to retrieve recipe info for ingredient ID {ingredient_id}")
            else:
                print("No ID found for the ingredient")

        # Create Recipe object
        print(data)
        recipe_data = {
            'nutrition': nutrition,
            'title': data.get('title'),
            'image': data.get('image'),
            'readyInMinutes': data.get('readyInMinutes'),
            'instructions': data.get('instructions'),
            'spoonacular_id': data.get('id'),
            'sourceName': data.get('sourceName'),
            'sourceUrl': data.get('sourceUrl'),
            'healthScore': data.get('healthScore'),
            'spoonacularScore': data.get('spoonacularScore'),
            'pricePerServing': data.get('pricePerServing'),
            'analyzedInstructions': data.get('analyzedInstructions'),
            'cheap': data.get('cheap'),
            'creditsText': data.get('creditsText'),
            'cuisines': data.get('cuisines'),
            'dairyFree': data.get('dairyFree'),
            'diets': data.get('diets'),
            'gaps': data.get('gaps'),
            'glutenFree': data.get('glutenFree'),
            'instructions': data.get('instructions'),
            'ketogenic': data.get('ketogenic'),
            'lowFodmap': data.get('lowFodmap'),
            'occasions': data.get('occasions'),
            'sustainable': data.get('sustainable'),
            'vegan': data.get('vegan'),
            'vegetarian': data.get('vegetarian'),
            'veryHealthy': data.get('veryHealthy'),
            'veryPopular': data.get('veryPopular'),
            'whole30': data.get('whole30'),
            'weightWatcherSmartPoints': data.get('weightWatcherSmartPoints'),
            'dishTypes': data.get('dishTypes'),
            'extendedIngredients': ingredients_data,
            'summary': data.get('summary'),
            'winePairing': data.get('winePairing'),
        }

        recipe = Recipe.objects.create(**recipe_data)
        # Serialize the recipe data
        serialized_recipe = RecipeSerializer(recipe).data
        return Response(serialized_recipe, status=status.HTTP_201_CREATED)

    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def fetch_filtered_recipes(request):
    filters = request.GET.dict()
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': settings.API_KEY,
        **filters  # Pass the filters as URL parameters
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return Response(data["results"])
    except requests.RequestException as e:
        status_code = response.status_code if response else 500
        return Response({'error': str(e)}, status=status_code)


import json
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseServerError

def fetch_recipes_by_name(request, name):
    try:
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={settings.API_KEY}&query={name}&sort=popularity"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return JsonResponse(data['results'], safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def update_nutrition_for_recipe(request):
    if request.method == 'POST':
        # Retrieve recipe ID and new nutrition data from POST request
        recipe_id = request.POST.get('recipeID')
        new_nutrition_data = request.POST.get('newNutrition')
        
        if new_nutrition_data:
            try:
                # Parse the JSON string into a dictionary
                new_nutrition_dict = json.loads(new_nutrition_data)
                
                # Retrieve the Recipe instance
                recipe = get_object_or_404(Recipe, pk=recipe_id)
                
                # Retrieve the associated Nutrition instance for the Recipe
                nutrition = recipe.nutrition
                
                if nutrition:
                    # Update the Nutrition instance fields based on new nutrition data
                    nutrition.nutrients = new_nutrition_dict.get('nutrients', [])
                    nutrition.properties = new_nutrition_dict.get('properties', [])
                    nutrition.flavonoids = new_nutrition_dict.get('flavonoids', [])
                    nutrition.caloric_breakdown = new_nutrition_dict.get('caloricBreakdown', {})
                    nutrition.weight_per_serving = new_nutrition_dict.get('weightPerServing', {})
                    
                    # Save the updated Nutrition instance
                    nutrition.save()
                    
                    return JsonResponse({'success': True, 'message': 'Nutrition updated successfully'})
                else:
                    return JsonResponse({'error': 'Nutrition instance not found for this recipe'}, status=404)
                
            except json.JSONDecodeError as e:
                # Handle JSON decoding error
                return JsonResponse({'error': str(e)}, status=400)
            
            except Recipe.DoesNotExist:
                # Handle Recipe not found error
                return JsonResponse({'error': 'Recipe not found'}, status=404)
        
        else:
            return JsonResponse({'error': 'No newNutrition data received'}, status=400)
    
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)