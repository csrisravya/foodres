from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import render

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    food_capacity_needed = models.IntegerField(validators=[MinValueValidator(1)])
    FOOD_PREFERENCE_CHOICES = (
    ('V', 'Veg'),
    ('N', 'Non Veg'),
    ('B', 'Both'),)
    food_preference = models.CharField(max_length=1, choices=FOOD_PREFERENCE_CHOICES)

