"""Views Imports """
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, View, ListView, DeleteView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.db.models import Count
from django.http import Http404
import requests
from .models import Category, Post, Comment
from .forms import CommentForm, InsightForm


# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument


class HomeView(ListView):
    """
    A view class for displaying the home page.
    """
    model = Post
    template_name = 'index.html'
    context_object_name = 'insights'

    queryset = Post.objects.filter(
        status=1).annotate(like_count=Count('likes')).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_insights'] = self.queryset[:2]
        context['most_popular'] = self.queryset.order_by('-like_count')[:2]
        return context


class InsightAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new insight post
    """
    model = Post
    template_name = "insights/add-insight.html"
    form_class = InsightForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new post
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)

        if form.instance.status == 0:
            success_message = "Insight added successfully! Waiting for Admin approval."
        elif form.instance.status == 2:
            success_message = "Insight added to drafts successfully."
        elif form.instance.status == 1:
            success_message = "Insight posted successfully."

        response = super().form_valid(form)
        messages.success(self.request, success_message)
        return response

    def form_invalid(self, form):
        """
        Handles form validation when creating a new post
        """
        response = super().form_invalid(form)
        messages.error(self.request, "Try Again. Please check all fields.")
        return response


class InsightDetailsView(View):
    """
    View for displaying the details of a specific post and adding comments.
    """
    template_name = "insights/insight-detail.html"

    def get(self, request, slug, *args, **kwargs):
        """
        Handle GET requests to display the details of a specific post and its comments.
        """
        try:
            post = get_object_or_404(Post, slug=slug)
        except Http404:
            return redirect('insights')

        comments = post.comments.order_by("-created_on")
        liked = (
            post.likes.filter(id=self.request.user.id).exists()
            if request.user.is_authenticated
            else False
        )
        favourited = (
            post.favourite.filter(id=self.request.user.id).exists()
            if request.user.is_authenticated
            else False
        )
        context = {

            "post": post,
            "liked": liked,
            "favourited": favourited,
            "comments": comments,
            "comment_form": CommentForm(),
            "commented": False,
        }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        """
        Handle POST requests to add a comment to the specific post.
        """
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by("-created_on")
        comment_form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to comment.")

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            post.comment_count = post.comments.count()
            post.save()
            messages.success(request, "Comment created successfully!")
            return redirect("insight-details", slug=post.slug)
        else:
            messages.error(request, "There was an error. Please try again!")

        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "commented": False,
        }
        return render(request, self.template_name, context)


class InsightsListView(ListView):
    """
    Base view for displaying insights with support for category filtering and search functionality.
    """
    model = Post
    template_name = 'insights/insights-list.html'
    context_object_name = 'insights'
    paginate_by = 6

    def get_queryset(self):
        """
        Filters the posts based on the search query and category.
        """
        query = self.request.GET.get("q")
        category_name = self.kwargs.get('category_name')

        posts = Post.objects.filter(status=1).order_by('-created_on')

        if query:
            posts = posts.filter(Q(content__icontains=query))

        if category_name:
            category = get_object_or_404(Category, name=category_name)
            posts = posts.filter(category=category)

        return posts

    def get_context_data(self, **kwargs):
        """
        Adds additional context data for categories and search query.
        """
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category_name')
        query = self.request.GET.get('q')

        if category_name:
            context['category'] = get_object_or_404(Category, name=category_name)

        context['categories'] = Category.objects.all()
        context['search_query'] = query

        return context


class SearchView(ListView):
    """
    A class-based view for displaying search results across all categories.
    """
    model = Post
    template_name = 'insights/search-results.html'
    context_object_name = 'insights'
    paginate_by = 6

    def get_queryset(self):
        """
        Filters the posts based on the search query.
        """
        query = self.request.GET.get("q", "")
        object_list = Post.objects.filter(status=1).order_by('-created_on')

        if query:
            object_list = object_list.filter(Q(content__icontains=query))

        return object_list

    def get_context_data(self, **kwargs):
        """
        Adds search query and categories to context data.
        """
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get("q", "")
        context['categories'] = Category.objects.all()
        return context


class CategoryFilterView(ListView):
    """
    View for displaying insights filtered by category.
    """
    model = Post
    template_name = 'insights/categories-search.html'
    context_object_name = 'insights'
    paginate_by = 6

    def get_queryset(self):
        """
        Filters the insights based on the category obtained from the URL.
        """
        category_name = self.kwargs.get('category_name')
        category = get_object_or_404(Category, name=category_name)
        object_list = Post.objects.filter(status=1, category=category).order_by('-created_on')
        return object_list

    def get_context_data(self, **kwargs):
        """
        Adds additional context data for categories and category name.
        """
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category_name')
        category = get_object_or_404(Category, name=category_name)
        context['category'] = category
        context['categories'] = Category.objects.all()
        return context


class InsightDeleteView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    Delete insights by author or superuser
    """
    model = Post
    template_name = "insights/delete-modal.html"
    success_message = "Insight removed successfully"
    success_url = reverse_lazy("home")

    def test_func(self):
        """
        Ensure that only insight author or admin can delete the recodrd..
        """
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def get_success_url(self):
        """
        Redirect to the HTTP referrer if available, otherwise use the default success URL.
        """
        referrer = self.request.META.get('HTTP_REFERER')
        if referrer:
            try:
                response = requests.head(referrer, timeout=2)
                response.raise_for_status()
                return referrer
            except requests.RequestException:
                pass
        return self.success_url


class InsightUpdateView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    """
    Edit insights by author or superuser
    """
    model = Post
    form_class = InsightForm
    template_name = "insights/insight-update.html"
    success_message = "Insight was edited successfully"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if not form.instance.author:
            form.instance.author = self.request.user

        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("insight-details", kwargs={"slug": self.object.slug})

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def form_invalid(self, form):
        """
        Handles form validation when creating a new post
        """
        response = super().form_invalid(form)
        messages.error(self.request, "Try Again. Please check all fields.")
        return response


class LikeInsightView(LoginRequiredMixin, View):
    """
    A view that handles the liking and unliking of a post by a user.
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Toggle user's like for a post and redirect to post detail
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(
                self.request,
                "Insight Unliked!")
        else:
            post.likes.add(request.user)
            messages.success(
                self.request,
                "Thank You for Liking!")
        referer = request.META.get('HTTP_REFERER')

        return redirect(referer)


class FavouriteInsightView(LoginRequiredMixin, ListView):
    """
    A view that handles the favouriting and unfavouriting of a post by a user.
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Handle the POST request to favourite or unfavourite a post.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.favourite.filter(id=self.request.user.id).exists():
            post.favourite.remove(request.user)
            messages.success(
                self.request,
                "Insight Removed from Favourites")
        else:
            post.favourite.add(request.user)
            messages.success(
                self.request,
                "Insight Added to Favourites List!")

        referer = request.META.get('HTTP_REFERER')

        return redirect(referer)

class CommentDeleteView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):

    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Comment
    template_name = "comments/delete_comment.html"
    success_message = "Comment removed successfully"

    def test_func(self):
        """
        Ensure that only the comment author or admin can delete the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_superuser

    def get_success_url(self):
        """
        Redirect to the post detail view after a successful comment deletion.
        """
        post = self.object.post
        return reverse_lazy("insight-details", kwargs={"slug": post.slug})


class CommentEditView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    """
    This view is used to allow logged in users and admin to update their own comments
    """
    model = Comment
    form_class = CommentForm
    template_name = "comments/edit-comment.html"
    success_message = "Comment updated successfully"

    def test_func(self):
        """
        Ensure that only the comment author or admin can delete the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_superuser

    def get_success_url(self):
        """
        Redirect to the post detail view after a successful comment deletion.
        """
        post = self.object.post
        return reverse_lazy("insight-details", kwargs={"slug": post.slug})


class PendingApprovalListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view for displaying a list of posts pending approval by admins.
    """
    model = Post
    template_name = 'insights/pending-approval-list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status=0).order_by('-created_on')

    def test_func(self):
        return self.request.user.is_superuser


class ApprovePostView(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    A view for displaying a list of posts pending approval by admins.
    """
    def post(self, request, pk, *args, **kwargs):
        """
        Handles HTTP POST requests to approve a post with the specified pk.
        If the post is pending (status=0), changes its status to approved (status=1).
        Redirects to the 'pending-posts' URL after approval.
        """
        post = get_object_or_404(Post, pk=pk)
        if post.status == 0:
            post.status = 1
            post.save()
            messages.success(request, f'Post "{post.title}" has been approved.')
        else:
            messages.info(request, f'Post "{post.title}" is already approved.')

        return redirect('pending-insights')

    def test_func(self):
        return self.request.user.is_superuser
