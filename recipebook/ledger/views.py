from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {"recipes": recipes})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    return render(request, 'ledger/recipe_detail.html', {
        "recipe": recipe,
    })

