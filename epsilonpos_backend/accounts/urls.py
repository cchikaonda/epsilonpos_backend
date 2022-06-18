from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', user_list, name = 'user_list'), 

]