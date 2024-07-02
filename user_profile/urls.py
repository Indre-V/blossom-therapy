"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
path(
    "profile/<str:username>/",
     views.ProfilePageView.as_view(),
     name="profile"),
path(
    "profile/<int:pk>/delete",
     views.ProfileDeleteView.as_view(),
     name="profile-delete"),
path(
    "profile/<int:pk>/update",
     views.ProfileUpdateView.as_view(),
     name="profile-update"),
path(
    "profile/<str:username>/insights/",
     views.ProfileInsightsView.as_view(),
     name='profile-insights'),
path(
    "profile/<str:username>/favourites/",
     views.ProfileFavouritesView.as_view(),
     name='profile-favourites'),
path(
    "profile/<str:username>/drafts/",
     views.ProfileDraftsView.as_view(),
     name='profile-drafts'),
]
