from django.views.generic import ListView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import DeveloperProfile
from .forms import ContactForm

# pylint: disable=locally-disabled, no-member

class DeveloperProfileView(SuccessMessageMixin, ListView, FormView):
    """
    Retrieve all DeveloperProfile instances and handle contact form submissions.

    This view combines ListView to display DeveloperProfile instances and FormView to handle
    the contact form. It manages both GET requests for displaying data and POST requests
    for form submission.
    """
    model = DeveloperProfile
    template_name = 'developer/developer_profile.html'
    context_object_name = 'developer_profiles'
    form_class = ContactForm
    success_url = reverse_lazy('developer_profile')
    success_message = "Your message has been sent successfully!"

    def get_queryset(self):
        """
        Return the list of DeveloperProfile instances for the ListView.
        """
        return DeveloperProfile.objects.all()

    def get_context_data(self, **kwargs):
        """
        Add the form to the context.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        """
        Handle valid form submission, save the form, 
        and re-render the page with the updated context.
        """
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form submission and re-render the page with the form and errors.
        """
        return self.render_to_response(self.get_context_data(form=form))
