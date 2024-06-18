"""URL Patterns"""
from django.urls import path
from . import views

urlpatterns = [
path('developer/', views.developer_profile_view, name='developer'),
path('contact/', views.contact, name='contact'),

]
