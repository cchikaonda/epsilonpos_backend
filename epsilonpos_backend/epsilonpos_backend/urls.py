from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')), 

    path('api/v1/', include('accounts.urls')), 
    path('api/v1/', include('stock.urls')),
    path('api/v1/', include('pos.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
