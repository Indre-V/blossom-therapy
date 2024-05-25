from django.shortcuts import render
from django.http import HttpResponse

def developer_view(request):
    return HttpResponse("Developer Section")
