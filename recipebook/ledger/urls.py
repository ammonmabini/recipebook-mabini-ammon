from django.urls import path
from .views import recipe_detail, recipe_list

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/<str:recipe_name>/', recipe_detail, name='recipe_detail'),
    ]

app_name = 'ledger'