from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args, **kwargs): #Python args and key word args
    return HttpResponse("<h1>Hello World</h1>") #string of HTML code