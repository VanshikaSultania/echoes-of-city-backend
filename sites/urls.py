from django.urls import path
from .views import HeritageSiteListView, HeritageSiteDetailView, ReviewCreateView

urlpatterns = [
    path('', HeritageSiteListView.as_view(), name='heritage-site-list'),
    path('<slug:site_id>/', HeritageSiteDetailView.as_view(), name='heritage-site-detail'),
    path('<slug:site_id>/reviews/', ReviewCreateView.as_view(), name='site-review-create'),
]
