from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')), 

    path('api/v1/accounts/', include('apps.accounts.urls')), 
    path('api/v1/stock/', include('apps.stock.urls')),
    path('api/v1/pos/', include('apps.pos.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)