"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('insights/', views.InsightsList.as_view(), name='insights'),
    path('profile/<str:username>/', views.ProfilePageView.as_view(), name='profile'),
    path(
        "profile_delete/<int:pk>/",
        views.ProfileDeleteView.as_view(),
        name="profile_delete",
    ),
      path(
        "profile_update/<int:pk>/",
        views.ProfileUpdateView.as_view(),
        name="profile_update",
    ),
    path('category/<str:category_name>/', views.CategoryPage.as_view(), name='category_posts'),
    path('post/add/', views.InsightCreateView.as_view(), name='add_post'),
    
]
