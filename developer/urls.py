"""URL Patterns"""
from django.urls import path
from .views import DeveloperProfileView

urlpatterns = [
    path('developer/', DeveloperProfileView.as_view(), name='developer_profile'),
]

