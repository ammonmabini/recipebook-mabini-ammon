from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[MinLengthValidator(256)])

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipe_list',
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', kwargs={'pk': self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', kwargs={'pk': self.pk})


class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
    )
