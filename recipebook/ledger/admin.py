from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile, Recipe, RecipeIngredient


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ("name",)
    list_display = ("name",)
    list_filter = ("name",)
    readonly_fields = ('created_on', 'updated_on')
    fieldsets = [
        ("Details", {
            'fields': [
                'name',
                'ingredients',
                'quantity',
                'author',
                'created_on',
                'updated_on',
                'recipe_image',
            ]
        }),
    ]
    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)
