"""URL Imports"""
from django.urls import path
from .views import DevProfileView, ContactFormView

urlpatterns = [
    path('about/', DevProfileView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
