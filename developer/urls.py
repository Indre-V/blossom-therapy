"""URL Patterns"""
from django.urls import path
from . import views

urlpatterns = [
path('developer/', views.developer, name='developer'),

]
