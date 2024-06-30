"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("insights/", views.InsightsListView.as_view(), name="insights"),
    path("search/", views.SearchResultsView.as_view(), name="search-results"),
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
        "category/<str:category_name>/",
        views.InsightsListView.as_view(),
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
         name='like-insight'),
    path("favourite/<slug:slug>/",
         views.FavouriteInsightView.as_view(),
         name='favourite-insight'),
    path("posts/pending/",
         views.PendingApprovalListView.as_view(),
         name='pending-posts'),
    path("posts/approve/<int:pk>/",
         views.ApprovePostView.as_view(),
         name='approve-post'),

]
