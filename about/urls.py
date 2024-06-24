"""URL Patterns"""
from django.urls import path
from .views import DevProfileView

urlpatterns = [
    path('about/', DevProfileView.as_view(), name='dev_profile'),
]
