from .models import Food
from fatsecret import Fatsecret

api_key = "2a56ae2c434b429dbaaae13b500041c4"
api_secret = "242498e295b042a69c470fb4612fdf0a"

fs = Fatsecret(api_key, api_secret)
base_google_url = "http://www.google.com/search?q="
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

# Called in views.py to get info of the food either from database or API
def get_food_info(food):
	results = Food.objects.filter(name=food)
	if results.count() == 0:
		calories, serving_size = get_food_nutrition_from_API(food)
	else:
		food_object = results[0]
		calories, serving_size = food_object.calories, food_object.serving_size

	return calories, serving_size

# Function to get food info from API if it is not in the database
def get_food_nutrition_from_API(food_query):

	foods = fs.foods_search(food_query)

	print foods
	
	calories = 0

	# Get top food result from API JSON results
	if len(foods) > 0: 
		food = foods[0]
		description = food['food_description']
		description = description.split('kcal')[0]
		calories = int(description.split('Calories: ')[-1])
		serving_size = food['food_description']
		serving_size = serving_size.split(' - ')[0]
		print "calories = {0}".format(calories)

	Food.objects.create(name=food_query, calories=calories, serving_size=serving_size)

	return calories, serving_size
