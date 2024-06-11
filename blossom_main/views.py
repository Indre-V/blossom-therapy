"""Views Imports """
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, View, ListView, DeleteView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .models import Category, Post, Comment
from .forms import CommentForm, InsightForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument
# pylint: disable=unused-variable

class HomeView(ListView):
    """
    A view class for displaying all posts on the home page.
    """
    model = Post
    queryset = Post.objects.all().filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 4
    context_object_name = 'insights'


class CategoryPageView(ListView):
    """
    A view class for displaying a list of posts based on a specific category.
    """
    model = Post
    template_name = "category.html"
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


class InsightAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new blog post
    """
    model = Post
    template_name = "insights/add_insight.html"
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


class InsightsListView(ListView):
    """
    View for creating a new blog post
    """
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "insights/insights_list.html"
    context_object_name = "insights"
    success_url = reverse_lazy("home")
    paginate_by = 6


class InsightDetailsView(View):
    """
    View for displaying the details of a specific post (insight) and adding comments.
    """
    template_name = "insights/insight_detail.html"

    def get(self, request, slug, *args, **kwargs):
        """
        Handle GET requests to display the details of a specific post and its comments.
        """
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = post.likes.filter(id=self.request.user.id).exists() if request.user.is_authenticated else False
        favourited = post.favourite.filter(id=self.request.user.id).exists() if request.user.is_authenticated else False
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

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            post.comment_count = post.comments.count()
            post.save()
            messages.success(request, "Comment created successfully!")
            return redirect('insight-details', slug=post.slug)
        else:
            messages.error(request, "There was an error. Action not registered!")

        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "commented": False,
        }
        return render(request, self.template_name, context)


class CommentDeleteView(
        LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Comment
    template_name = "comments/delete_comment.html"
    success_message = "Comment deleted successfully"

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
    This view is used to allow logged in users to updatetheir own comments
    """
    model = Comment
    fields = ["content"]
    template_name = "comments/edit_comment.html"
    success_message = "Comment updated successfully"

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy("insight-details", kwargs={"slug": post.slug})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_superuser

class InsightDeleteView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    """
    Delete insights by author or superuser
    """
    model = Post
    template_name = "insights/insight_delete.html"
    success_message = "Insight removed successfully"
    success_url = reverse_lazy("insights")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser


class InsightUpdateView(
        LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    """
    Edit insights by author or superuser
    """
    model = Post
    form_class = InsightForm
    template_name = "insights/insight_update.html"
    success_message = "%(calculated_field)s was edited successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("insight-details", kwargs={"slug": self.object.slug})

    def get_success_message(self, cleaned_data):
        """
        Override the get_success_message() method to add the recipe title
        into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )

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
        return HttpResponseRedirect(reverse("insight-details", args=[slug]))

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
        return HttpResponseRedirect(reverse("insight-details", args=[slug]))
