# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Food

from .calorie_counter import get_food_info

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_foods=Food.objects.all().count()

    context = {
    	'num_foods': num_foods
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

def get_cal_count(request):
	"""
	Function to get cal count of food using FatSecret API
	"""

	if request.method == "POST":
		food = request.POST['food']
		if food and len(food) > 0:
			calories, serving_size = get_food_info(food)
			calories_message = food + ": " + str(calories) + " calories " + str(serving_size)
			messages.add_message(request, messages.INFO, calories_message)	

	return HttpResponseRedirect('/')
	# return render(None, 'index.html', context={'num_foods': num_foods, 'num_calories': calories})
