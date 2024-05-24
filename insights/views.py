from django.shortcuts import render
from django.http import HttpResponse

def my_insights(request):
    return HttpResponse("Hello, Insights!")
