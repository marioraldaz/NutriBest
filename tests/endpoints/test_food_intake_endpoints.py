from food_intake.food_intake_detail import FoodIntakeDetail
import pytest
from django.urls import reverse
from factories.user_profile_factory import UserProfileFactory 
from django.utils import timezone
from factories.food_intake_factory import FoodIntakeFactory
from django.shortcuts import HttpResponse
from food_intake.food_intake import FoodIntake
#####################################################################################TESTS FOR FOOD_INTAKE_LIST#########################################################################################################    

#Test endpoint works
@pytest.mark.django_db
def test_save_food_intake(client):
    url = reverse('food_intake_list') 
  
    response = client.get(url)

    print (response)
    # Assert that the response is as expected
    assert response.status_code == 200
    
##############################################################################################################################################################################################    





###################################################################################TESTS FOR /FOOD_INTAKE_DETAIL/#################################################################################################    

@pytest.mark.xfail
@pytest.mark.django_db
def test_food_intake_detail(client, food_intake_detail):
    # Create a food intake instance using the factory
    object_detail = food_intake_detail
    print(object_detail)
    
    FoodIntakeDetail.objects.create(object)

    # Get the URL for the food_intake_detail view with the food intake's pk
    url = reverse('food_intake_detail', kwargs={'pk': object.pk}) + 'details/'

    # Make a GET request to the URL using the test client
    response = client.get(url)
    print(url)
    # Check that the response status code is 200 OK
    assert response.status_code == HttpResponse.status_code

    assert len(response.content) > 0  # Assuming the response has content
    
##############################################################################################################################################################################################    


##################################################################################TESTS FOR /FOOD_INTAKE_LIST/ #############################################################################################    



#CHECKING STATUS CODE CORRECT FOR SIMPLE GET 
@pytest.mark.django_db
def test_food_intake_list(client):
    # Create some food intake instances using the factory
    FoodIntakeFactory.create_batch(5)

    # Get the URL for the food_intake_list view
    url = reverse('food_intake_list')

    # Make a GET request to the URL using the test client
    response = client.get(url)

    # Check that the response status code is 200 OK
    assert response.status_code == HttpResponse.status_code

    # Check other assertions as needed based on your view's behavior
    assert len(response.content) > 0 
    
    
    
#USING MONKEYPATCH FOR SIMPLE GET STATUS CODE CHECK
@pytest.mark.django_db
def test_food_intake_list_monkey(client, monkeypatch):
    # Create some fake FoodIntake instances using the factory
    food_intakes = FoodIntakeFactory.create_batch(5)

    # Define a mock function to replace FoodIntake.objects.all()
    def mock_food_intake_all():
        return food_intakes

    # Patch the FoodIntake.objects.all() method with the mock function
    monkeypatch.setattr(FoodIntake.objects, 'all', mock_food_intake_all)

    # Get the URL for the food_intake_list view
    url = reverse('food_intake_list')

    # Make a GET request to the URL using the test client
    response = client.get(url)

    # Check that the response status code is 200 OK
    assert response.status_code == HttpResponse.status_code

    # Check other assertions as needed based on your view's behavior
    assert len(response.content) > 0  # Assuming the response has content



#USING MONKEYPATCH TO CHECK IF HTTP RETURNS "PROFILE REQUIRED" WHEN IT IS NOT IN THE REQUEST
"""_summary_


@pytest.mark.django_db
def test_simulate_exception(monkeypatch):
    # Define a mock function that raises a ValueError for missing profile
    def mock_create_food_intake(*args, **kwargs):
        if 'profile' not in kwargs:
            raise ValueError("Profile is required")
        return FoodIntake.objects.create(*args, **kwargs)

    # Monkeypatch the FoodIntake.objects.create method with our mock function
    monkeypatch.setattr(FoodIntake.objects, 'create', mock_create_food_intake)

    # Create a test request with POST data missing 'profile'
    post_data = {'meal_type': 'Breakfast'}  # Only include meal_type, omit profile
    request = RequestFactory().post(reverse('food_intake_list'), post_data)

    # Call the view function with the test request
    response = food_intake_list(request)
   # Render the response content
    response.render()
    
    
    response_json = json.loads(response.content.decode())
    assert 'profile' in response_json  # Check if 'profile' is in the response JSON keys
    assert 'This field is required.' in response_json['profile']  # Check the error message in the 'profile' key

    # Assert that the response is a HttpResponse with status 400
    assert isinstance(response, HttpResponse)
    assert response.status_code == 400
"""

##############################################################################################################################################################################################    
    