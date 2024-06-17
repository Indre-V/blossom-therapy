from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import DeveloperProfile


def developer(request, username):
    developer_profile = get_object_or_404(DeveloperProfile, user__username=username)
    return render(request, 'developer/developer_profile.html', {'developer': developer_profile})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'developer/contact.html', {'form': form})