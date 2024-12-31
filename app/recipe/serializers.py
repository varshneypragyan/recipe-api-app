"""
Serializers for recipe APIs
"""

from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'title_minutes', 'price', 'link']
        read_only_fields = ['id']