from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .models import Profile
from django.urls import reverse_lazy




class Home(generic.TemplateView):
    """This view is used to display the home page"""
    template_name = "includes/base.html"


class ProfilePageView(generic.DetailView):
    template_name = "includes/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        """
        Retrieve the profile object based on the provided username.
        """
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return get_object_or_404(Profile, user=user)

    def get_context_data(self, **kwargs):
        """
        Prepares and adds additional context data for rendering
        the profile page.
        """
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['profile'] = profile
        context['user'] = profile.user
        return context

class ProfileDeleteView(generic.DeleteView):
    """
    View for deleting an user profile
    """
    model = User
    template_name = "includes/profile_delete.html"
    success_url = reverse_lazy("home")

    def delete(self, request, *args, **kwargs):
        """
        Handles the deletion of an user profile and related objects
        """
        # Log out the user
        logout(request)

        # Delete the user profile and related objects
        return super().delete(request, *args, **kwargs)