from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import UserForm, ProfileForm
from django.views.generic.edit import UpdateView





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

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View for updating user profile information.
    """
    model = Profile
    form_class = ProfileForm
    success_message = "Profile has been updated"
    template_name = "includes/profile_update.html"

    def get_object(self, queryset=None):
        """
        Returns the profile of the current user.
        """
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        """
        Returns the URL to redirect to after processing a valid form.
        """
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})

    def get_context_data(self, **kwargs):
        """
        Add user form to the context.
        """
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['user_form'] = UserForm(instance=self.request.user)
        else:
            context['user_form'] = UserForm(self.request.POST, instance=self.request.user)
        return context

    def form_valid(self, form):
        """
        If the form is valid, save the associated models.
        """
        context = self.get_context_data()
        user_form = context['user_form']
        if user_form.is_valid():
            user_form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)