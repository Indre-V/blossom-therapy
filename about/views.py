"""About Imports"""
from django.views.generic import ListView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import DevProfile
from .forms import ContactForm

# pylint: disable=locally-disabled, no-member

class ContactFormView(SuccessMessageMixin, FormView):
    """
    View to handle the contact form submission.
    """
    form_class = ContactForm
    template_name = 'components/contact.html'
    success_url = reverse_lazy('home')
    success_message = "Your message has been sent successfully!"

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

class DevProfileView(ListView):
    """
    View to display developer profiles.
    """
    model = DevProfile
    template_name = 'about/dev-details.html'
    context_object_name = 'dev_profiles'

    def get_queryset(self):
        """
        Return the queryset of DeveloperProfile instances.
        """
        return DevProfile.objects.all()