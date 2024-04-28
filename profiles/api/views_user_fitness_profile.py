from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.user_profile import UserProfile
from profiles.profile_fitness import UserFitnessProfile
import json
from django.http import JsonResponse

@login_required
def fitness_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    try:
        fitness_profile = user_profile.fitness_profile
    except UserFitnessProfile.DoesNotExist:
        # Create a new fitness profile if it doesn't exist
        fitness_profile = UserFitnessProfile(user_profile=user_profile)
        fitness_profile.save()

    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
        try:
            data = json.loads(request.body)
            goal = data.get('goal')
            activity_level = int(data.get('activityLevel', 1))  # Default to 1 if not provided

            # Update fitness profile fields
            fitness_profile.goal = goal
            fitness_profile.activity_level = activity_level
            fitness_profile.save()

            # Calculate and set fitness goals based on updated profile
            fitness_profile.calculate_and_set_daily_calorie_intake_goal()
            fitness_profile.calculate_and_set_daily_protein_goal()
            fitness_profile.calculate_and_set_daily_fat_goal()
            fitness_profile.calculate_and_set_daily_carbohydrate_goal()

            # Return updated fitness profile data as JSON response
            return JsonResponse({
                'daily_calorie_intake_goal': fitness_profile.daily_calorie_intake_goal,
                'daily_protein_goal': fitness_profile.daily_protein_goal,
                'daily_fat_goal': fitness_profile.daily_fat_goal,
                'daily_carbohydrate_goal': fitness_profile.daily_carbohydrate_goal
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    # If not a POST request or invalid JSON payload, render the HTML template with context
    context = {
        'user_profile': user_profile,
        'fitness_profile': fitness_profile,
    }
    return render(request, 'fitness_profile.html', context)