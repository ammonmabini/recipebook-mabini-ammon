from django.urls import path

from .views import (
    RecipeAddImageView,
    RecipeAddView,
    RecipeDetailView,
    RecipeListView,
)

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path(
        'recipe/<int:pk>/',
        RecipeDetailView.as_view(),
        name='recipe_detail'
    ),
    path('recipe/add/', RecipeAddView.as_view(), name='recipe_form'),
    path(
        'recipe/<int:pk>/add_image/',
        RecipeAddImageView.as_view(),
        name='recipe_add_image'
    ),
]

app_name = 'ledger'
