# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    """
    Model representing a food (e.g. pizza, cucumber).
    """
    name = models.CharField(max_length=200, help_text="Enter a food item (e.g. pizza, cucumber, chicken..)")
    calories = models.IntegerField(default=0)
    serving_size = models.CharField(max_length=200, help_text="Enter the serving size", default=0)
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name