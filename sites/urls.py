from django.urls import path
from .views import HeritageSiteListView, HeritageSiteDetailView

urlpatterns = [
    path('', HeritageSiteListView.as_view(), name='heritage-site-list'),
    path('<slug:site_id>/', HeritageSiteDetailView.as_view(), name='heritage-site-detail'),
]
