from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index (request):
    return HttpResponse("Hello, world! To view the recipe list, go to /recipes/list/")

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {
        "recipes": recipes})

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'ledger/recipe_detail.html', {
        "recipe": recipe,
    })

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

