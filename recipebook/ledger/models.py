from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_list')

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', kwargs={'recipe_name': self.name})

class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, 
                                  related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, 
                                  related_name='ingredients')