from django.db import models
from food_intake.user_daily import UserDaily
from profiles.user_profile import UserProfile
from utils.validators import validate_meal_type
from django.utils.translation import gettext_lazy as _

class FoodIntake(models.Model): 
    MEAL_CHOICES = [
        ('Breakfast', _('Breakfast')),
        ('Lunch', _('Lunch')),
        ('Dinner', _('Dinner')),
        ('Snack', _('Snack')),
    ]
   
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    user_daily = models.ForeignKey(UserDaily, on_delete=models.CASCADE)
    meal_type = models.CharField(
         validators=[validate_meal_type],
        max_length=20, choices=MEAL_CHOICES
    )
    class Meta:
        db_table = 'profiles_foodintake' 
        
