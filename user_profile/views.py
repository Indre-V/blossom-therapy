"""Views Imports """
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, View
from blossom_main.models import Post
from .models import Profile
from .forms import UserForm, ProfileForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument
# pylint: disable=unused-variable

class ProfilePageView(LoginRequiredMixin, DetailView):
    """This view is used to display user profile page"""
    template_name = "profile/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        """
        Retrieve the profile object based on the provided username.
        """
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return get_object_or_404(Profile, user=user)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        user = profile.user
        insights = Post.objects.filter(author=user, status__in=[0, 1])
        drafts = Post.objects.filter(author=user, status=2)
        favourites = Post.objects.filter(favourite=user)
        total_likes = sum(post.count_likes() for post in insights)
        total_favourites = sum(post.count_favs() for post in insights)

        context.update({
            'profile': profile,
            'user': user,
            'insights': insights,
            'drafts': drafts,
            'favourites': favourites,
            'total_likes': total_likes,
            'total_favourites': total_favourites
        })
        return context

class ProfileFavouritesView(View):
    """
    View for display and manage user drafts
    """
    def get(self, request, username):
        """
        Renders the user's favourites page.
        """
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        favourites = Post.objects.filter(favourite=user)

        context = {
            'profile': profile,
            'favourites': favourites,
        }

        return render(request, 'profile/user_favourites.html', context)

class ProfileDraftsView(View):
    """
    View for display and manage user drafts
    """
    def get(self, request, username):
        """
        Renders the user's drafts page.
        """
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        drafts = Post.objects.filter(author=user, status=2)

        context = {
            'profile': profile,
            'drafts': drafts,
        }

        return render(request, 'profile/user_drafts.html', context)

class ProfileInsightsView(View):
    """
    View for display and manage user insights
    """
    paginate_by = 4
    def get(self, request, username):
        """
        Handles display render of the user insights
        """
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        insights = Post.objects.filter(author=user, status__in=[0, 1])
        context = {
            'profile': profile,
            'insights': insights,
        }

        return render(request, 'profile/user_insights.html', context)

class ProfileDeleteView(DeleteView):
    """
    View for deleting an user profile
    """
    model = User
    template_name = "profile/profile_delete.html"
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
    template_name = "profile/profile_update.html"

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
        return reverse_lazy("profile", kwargs={"username": self.request.user.username})

    def get_context_data(self, **kwargs):
        """
        Add user form to the context.
        """
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            context["user_form"] = UserForm(instance=self.request.user)
        else:
            context["user_form"] = UserForm(self.request.POST, instance=self.request.user)
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
