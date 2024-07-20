from django.shortcuts import render

# Create your views here.

def index(request): # new view function for index page
    return render(request, 'core/index.html')

def about(request): # new view function for about page
    return render(request, 'core/about.html')