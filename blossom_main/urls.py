"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/<str:username>/', views.ProfilePageView.as_view(), name='profile'),
]
