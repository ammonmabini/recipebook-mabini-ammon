from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
        inlines = [ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = [
        ('Details',{
            'fields': [
                ('name', 'created_on', 'updated_on'), 'author'
        ]
        }),
    ]
    inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)
