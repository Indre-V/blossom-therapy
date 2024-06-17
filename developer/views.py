from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def developer(request):
    return HttpResponse("Developer Section")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'developer/contact.html', {'form': form})