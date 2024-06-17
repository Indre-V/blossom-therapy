from django.shortcuts import render
from django.http import HttpResponse

def developer(request):
    return HttpResponse("Developer Section")
