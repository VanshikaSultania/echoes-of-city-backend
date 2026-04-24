"""
URL configuration for backend_config project.
"""
# from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/sites/', include('sites.urls')),
]
