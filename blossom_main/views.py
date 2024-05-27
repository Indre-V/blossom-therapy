from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Profile




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
