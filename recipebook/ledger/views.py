from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic import DetailView
from django.views.generic.list import ListView


def index(request):
    return HttpResponse('Welcome to my recipe book!')


recipes = []

def recipe_list(request):
    recipes = Recipe.objects.all() #fetches all tasks from database
    return render(request, 'ledger/recipe_list.html', {"recipes": recipes})

def recipe_detail(request, recipe_id):
    recipe = next((item for item in recipes 
                   if item["link"] == f"/recipe/{recipe_id}"), None)
    
    return render(request, 'ledger/recipe_detail.html', {"recipe": recipe})

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
