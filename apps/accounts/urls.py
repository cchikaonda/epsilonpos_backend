# apps/accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, custom_login, CustomObtainAuthToken, CustomLoginView

# Create a router and register the CustomUserViewSet
router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='accounts')

urlpatterns = [
    path('users', include(router.urls)),
    path('login', CustomLoginView.as_view(), name='login'),
    path('token', CustomObtainAuthToken.as_view(), name='obtain_token'),
]
