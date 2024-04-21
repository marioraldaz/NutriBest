from django.urls import path, include
from rest_framework import routers
from .views_ingredients_spoonacular import *
from .views_recipes_spoonacular import *
from rest_framework.documentation import include_docs_urls
from profiles.api import views
from .views import *
from .views_profile import *

#api versioning
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, 'user')


urlpatterns = [
    path('token/refresh/', refresh_token, name='token_refresh'),
    path("register/", register, name='register'),
    path("login/", login, name='login'),
    path("get_profile/", get_profile, name='get_profile'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('save-recipe', save_recipe, name="save_recipe"),
    path('get-saved-recipes', get_saved_recipes, name="get_saved_recipes"),
    path('unsave-recipe', unsave_recipe, name="unsave_recipe"),
    path('change-password/', change_password, name='change_password')
]
"""
    path('fetch-ingredients-by-name/<str:name>/', fetch_ingredients_by_name, name='fetch_ingredients_by_name'),
    path('get-ingredient-details/<int:ingredient_id>/<str:amount>/', fetch_ingredient_by_id, name='fetch_ingredient_by_id'),
    path('fetch-filtered-ingredients/', fetch_filtered_recipes, name='fetch_filtered_ingredients'),
    path('fetch-recipes-by-name/<str:name>/', fetch_recipes_by_name, name='fetch_recipes_by_name'),
    path('get-recipe-info/<int:id>/', get_recipe_info, name='get_recipe_info'),
    path('fetch-filtered-recipes/', fetch_filtered_recipes, name='fetch_filtered_recipes'),
    path('get-recipe-by-id/<int:recipe_id>/', get_recipe_by_id, name='get_recipe_by_id'),
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
