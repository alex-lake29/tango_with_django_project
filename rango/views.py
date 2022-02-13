from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Rango says hey there partner!\n<a href='/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    #return HttpResponse("Rango says here is about the page.\n<a href='/'>Back</a>")
    context_dict = {'boldmessage': 'Alex Lake!'}
    return render(request, 'rango/about.html', context=context_dict)