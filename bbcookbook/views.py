# Create your views here.
from django.views.generic.base import TemplateView
from bbcookbook.models import Meal
from rest_framework import serializers, generics
from bbcookbook.serializers import MealSerializer 
from rest_framework.views import APIView

class IndexView(TemplateView):

    template_name = 'index.html'

from bbcookbook.models import Meal
from bbcookbook.serializers import MealSerializer
from rest_framework import generics

class MealList(generics.ListCreateAPIView):
    model = Meal
    serializer_class = MealSerializer

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Meal
    serializer_class = MealSerializer

'''
class MealList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Meal 
    serializer_class = MealSerializer 

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Meal
    serializer_class = MealSerializer
'''


