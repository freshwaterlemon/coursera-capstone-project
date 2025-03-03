# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Car Model Model
class CarModel(models.Model):
    # Define car type choices
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    COUPE = "Coupe"
    CONVERTIBLE = "Convertible"
    HATCHBACK = "Hatchback"
    TRUCK = "Truck"

    CAR_TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (COUPE, "Coupe"),
        (CONVERTIBLE, "Convertible"),
        (HATCHBACK, "Hatchback"),
        (TRUCK, "Truck"),
    ]

    # Many-to-One
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="car_models"
    )
    name = models.CharField(max_length=100)
    car_type = models.CharField(
        max_length=20, choices=CAR_TYPE_CHOICES, default=SEDAN
    )
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    def __str__(self):
        return (
            f"{self.name} ({self.car_make.name}, {self.car_type}, {self.year})"
        )
