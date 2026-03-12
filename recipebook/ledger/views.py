from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView

from .models import Profile, Recipe, RecipeImage


def index(request):
    return HttpResponse(
        "Hello, world! To view the recipe list, go to /recipes/list/"
    )


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(
        request,
        'ledger/recipe_list.html',
        {
            "recipes": recipes,
        },
    )


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(
        request,
        'ledger/recipe_detail.html',
        {
            "recipe": recipe,
        },
    )


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'


class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_form.html'
    fields = ['name', ]

    def form_valid(self, form):
        form.instance.author = get_object_or_404(
            Profile, user=self.request.user
        )
        return super().form_valid(form)


class RecipeAddImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'ledger/recipe_add_image.html'
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe_detail',
            kwargs={'pk': self.object.recipe.pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(
            Recipe, pk=self.kwargs['pk']
        )
        return context
