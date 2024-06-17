"""URL Patterns"""
from django.urls import path
from . import views

urlpatterns = [
path('developer/<str:username>/', views.developer, name='developer'),
path('contact/', views.contact, name='contact'),

]
