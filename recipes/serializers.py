from rest_framework import serializers
from .models import Category, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'category', 'author', 'date_posted', 'ingredients', 'cooking_method',
                  'photo1', 'photo2', 'photo3', 'rating', 'in_category')
        extra_kwargs = {
            'photo1': {'required': False},
            'photo2': {'required': False},
            'photo3': {'required': False},
            'rating': {'required': False},
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'photo')
        extra_kwargs = {
            'photo': {'required': False},
        }
