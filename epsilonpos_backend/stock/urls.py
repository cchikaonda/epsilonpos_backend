from django.urls import path, include
from stock import views

urlpatterns = [
    path('items/', views.ItemsList.as_view()),
    path('item-categories/', views.ItemsCategoriesList.as_view()),
]