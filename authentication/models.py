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
    
    VEG = 'Veg'
    NON_VEG = 'Non Veg'
    BOTH = 'Both'

    FOOD_TYPE_CHOICES = (
        (VEG, 'Veg'),
        (NON_VEG, 'Non Veg'),
        (BOTH, 'Both'),
    )

    food_type = models.CharField(
        max_length=10,
        choices=FOOD_TYPE_CHOICES,
        default=VEG,
    )
    


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    VEG = 'Veg'
    NON_VEG = 'Non Veg'
    BOTH = 'Both'

    FOOD_TYPE_CHOICES = (
        (VEG, 'Veg'),
        (NON_VEG, 'Non Veg'),
        (BOTH, 'Both'),
    )

    fresh_food = models.BooleanField(default=False)
    food_remains = models.BooleanField(default=False)
    food_type = models.CharField(
        max_length=10,
        choices=FOOD_TYPE_CHOICES,
        default=VEG,
    )

    fresh_food_capacity = models.IntegerField(default=0)
    food_remains_capacity = models.IntegerField(default=0)
    description = models.TextField(blank=True)

