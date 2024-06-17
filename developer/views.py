"""Developer Profile Views"""
from django.shortcuts import render, redirect
from .models import DeveloperProfile
from .forms import ContactForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument
# pylint: disable=unused-variable


def developer_profile_view(request):
    """
    View function to display the developer profile.
    
    Retrieves the DeveloperProfile associated with a Profile marked as a developer.
    Renders 'developer/developer_profile.html' template with developer_profile context.
    """
    try:
        developer_profile = DeveloperProfile.objects.select_related(
            'user__profile').get(user__profile__is_developer=True)
    except DeveloperProfile.DoesNotExist:
        developer_profile = None

    context = {
        'developer_profile': developer_profile
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
            return redirect('success')  # Replace 'success' with the appropriate URL name
    else:
        form = ContactForm()

    return render(request, 'developer/contact.html', {'form': form})
