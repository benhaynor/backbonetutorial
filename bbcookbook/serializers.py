from rest_framework import serializers
from bbcookbook.models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
