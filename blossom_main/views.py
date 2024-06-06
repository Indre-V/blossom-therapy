from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .models import Profile, Category, Post, Comment
from .forms import UserForm, ProfileForm, CommentForm, InsightForm



class Home(generic.ListView):
    """
    A view class for displaying all posts on the home page.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = "posts"
    paginate_by = 10


class ProfilePageView(generic.DetailView):
    """This view is used to display user profile page"""
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

class CategoryPage(generic.ListView):
    """
    A view class for displaying a list of posts based on a specific category.
    """
    model = Post
    template_name = "category.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        """
        Filters the posts based on the category obtained from the URL.
        """
        category_name = self.kwargs['category_name']
        category = get_object_or_404(Category, name=category_name)
        return Post.objects.filter(category=category, status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, name=self.kwargs['category_name'])
        return context


class InsightCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new blog post
    """
    model = Post
    template_name = "includes/add_insight.html"
    form_class = InsightForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new post
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        messages.success(self.request, "Post created successfully! Waiting for Admin approval")
        return response

    def form_invalid(self, form):
        """
        Handles form validation when creating a new post
        """
        response = super().form_invalid(form)
        messages.error(self.request, "Post creation failed. Please check your input.")
        return response

class InsightsList(ListView):
    """
    View for creating a new blog post
    """
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "includes/insights_list.html"
    context_object_name = "insight_list"
    success_url = reverse_lazy("home")

class InsightDetails(generic.View):
    """
    View for displaying the details of a specific post (insight) and adding comments.
    """
    template_name = "includes/insight_detail.html"

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        context = {
            "post": post,
            "comments": comments,
            "comment_form": CommentForm(),
            "commented": False,
        }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(
                self.request,
                "Comment created successfully!"
            )
        else:
            messages.error(
                self.request,
                "There was an error. Action not registered!")

        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "commented": False,
        }
        return render(request, self.template_name, context)

class DeleteCommentView(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):

    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Comment
    template_name = 'includes/delete_comment.html'
    success_message = "Comment deleted successfully"

    def test_func(self):
        """
        Ensure that only the comment author can delete the comment.
        """
        comment = self.get_object()
        return comment.author == self.request.user
    
    def get_success_url(self):
        """
        Redirect to the post detail view after a successful comment deletion.
        """
        post = self.object.post
        return reverse_lazy('insight_details', kwargs={'slug': post.slug}) 

class EditCommentView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):

    """
    This view is used to allow logged in users to updatetheir own comments
    """
    model = Comment
    fields = ['content']
    template_name = 'includes/edit_comment.html'
    success_message = "Comment updated successfully" 

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('insight_details', kwargs={'slug': post.slug}) 

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

class InsightDeleteView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    """
    Delete insights by author or superuser
    """
    model = Post
    template_name = 'includes/insight_delete.html'
    success_message = "Insight removed successfully"

    def get_success_url(self):
        return reverse_lazy('insights')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

