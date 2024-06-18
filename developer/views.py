"""Developer Profile Views"""
from django.shortcuts import render, redirect
from .models import DeveloperProfile
from .forms import ContactForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument
# pylint: disable=unused-variable


def developer_profile_view(request):
    """
    Retrieve all DeveloperProfile instances
    """
    developer_profiles = DeveloperProfile.objects.all()

    context = {
        'developer_profiles': developer_profiles
    }

    return render(request, 'developer/developer_profile.html', context)

def contact(request):
    """
    View function to handle contact form submission and display contact form.
    
    Displays a contact form to submit data. On form submission (POST), saves the form data
    and redirects to 'success' URL upon successful validation.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'developer/contact.html', {'form': form})
