import imp
from unicodedata import category
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Item, ItemCategory, Stock, Supplier
from .serializers import ItemSerializer, ItemCategorySerializer

class ItemsList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        selializer = ItemSerializer(items, many=True)
        return Response(selializer.data)

class ItemsCategoriesList(APIView):
    def get(self, request, format=None):
        item_categories = ItemCategory.objects.all()
        selializer = ItemCategorySerializer(item_categories, many=True)
        return Response(selializer.data)

