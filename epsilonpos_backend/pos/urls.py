from django.db import router
from django.urls import path
from django.contrib.auth import views as auth_views
from pos.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers
router = routers.SimpleRouter()

urlpatterns = [
    path('', pos_dashboard, name = 'pos_dashboard'), 
]