# apps/accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, custom_login, CustomObtainAuthToken, CustomLoginView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('token/', CustomObtainAuthToken.as_view(), name='obtain_token'),
]

