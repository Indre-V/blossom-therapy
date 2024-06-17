from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def developer(request):
    return HttpResponse("Developer Section")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'developer/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'developer/contact.html', context)