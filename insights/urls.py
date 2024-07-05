"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "insights/",
         views.InsightsListView.as_view(),
         name="insights"),
    path(
        "insight/add/",
        views.InsightAddView.as_view(),
        name="add-insight"),
    path(
        "insight/update/<slug:slug>",
        views.InsightUpdateView.as_view(),
        name="insight-update"),
    path(
        "insight/delete/<slug:slug>",
        views.InsightDeleteView.as_view(),
        name="insight-delete"),
    path(
        "insights/<slug:slug>/",
        views.InsightDetailsView.as_view(),
        name="insight-details"),
    path(
        "search/", 
        views.SearchView.as_view(),
        name="search"),
    path(
        "categories/<str:category_name>/", 
        views.CategoryFilterView.as_view(),
        name="category-posts"),
    path(
        "comments/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="delete-comment"),
    path(
        "comments/<int:pk>/edit/",
        views.CommentEditView.as_view(),
        name="edit-comment"),
    path(
        "like/<slug:slug>/",
         views.LikeInsightView.as_view(),
         name='like-insight'),
    path(
        "favourite/<slug:slug>/",
         views.FavouriteInsightView.as_view(),
         name='favourite-insight'),
    path(
        "pending/insights",
         views.PendingApprovalListView.as_view(),
         name='pending-insights'),
    path(
        "approve/insights/<int:pk>/",
         views.ApprovePostView.as_view(),
         name='approve-insight'),
]
