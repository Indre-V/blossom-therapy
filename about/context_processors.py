""" Import for Context Processors"""
from .forms import ContactForm

def contact_form(request):
    return {'contact_form': ContactForm()}
