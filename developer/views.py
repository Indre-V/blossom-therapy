"""Developer Profile Views"""
from django.shortcuts import render, redirect
from .models import DeveloperProfile
from .forms import ContactForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument
# pylint: disable=unused-variable


def developer_profile_view(request):
    """
    Retrieve all DeveloperProfile instances and handle contact form.
    """
    developer_profiles = DeveloperProfile.objects.all()
    success_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Your message has been sent successfully!"
            form = ContactForm()  # Reset the form
    else:
        form = ContactForm()

    context = {
        'developer_profiles': developer_profiles,
        'form': form,
        'success_message': success_message
    }

    return render(request, 'developer/developer_profile.html', context)
