from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {"recipes": recipes})

def recipe_detail(request, recipe_name):
    recipe = Recipe.objects.get(name=recipe_name)

    return render(request, 'ledger/recipe_detail.html', {
        "recipe": recipe,
    })
