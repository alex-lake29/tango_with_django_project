from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner!\n<a href='/about/'>About</a>")
def about(request):
    return HttpResponse("Rango says here is about the page.\n<a href='/'>Back</a>")