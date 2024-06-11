"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("insights/", views.InsightsListView.as_view(), name="insights"),
    path(
        "profile/<str:username>/",
        views.ProfilePageView.as_view(), name="profile"),
    path(
        "insight/add/",
        views.InsightAddView.as_view(),
        name="add-insight"),
    path(
        "insights/<slug:slug>/",
        views.InsightDetailsView.as_view(),
        name="insight-details"),
    path(
        "insight/<slug:slug>/delete/",
        views.InsightDeleteView.as_view(),
        name="insight-delete"),
    path(
        "insight/<slug:slug>/update/",
        views.InsightUpdateView.as_view(),
        name="insight-update"),
    path(
        "profile_delete/<int:pk>/",
        views.ProfileDeleteView.as_view(),
        name="profile-delete"),
    path("profile_update/<int:pk>/",
         views.ProfileUpdateView.as_view(),
         name="profile-update"),
    path(
        "category/<str:category_name>/",
        views.CategoryPageView.as_view(),
        name="category-posts"),
    path(
        "comments/<int:pk>/delcomment/",
        views.CommentDeleteView.as_view(),
        name="delete-comment"),
    path(
        "comments/<int:pk>/editcomment/",
        views.CommentEditView.as_view(),
        name="edit-comment"),
    path("like/<slug:slug>/",
         views.LikeInsightView.as_view(),
         name='like-post'),
    path("favourite/<slug:slug>/",
         views.FavouritePostView.as_view(),
         name='favourite_post'),
]
