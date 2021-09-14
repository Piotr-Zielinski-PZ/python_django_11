from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    """Food class."""

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        """Class object represented in string."""
        return self.name


class Consume(models.Model):
    """Consume class."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
