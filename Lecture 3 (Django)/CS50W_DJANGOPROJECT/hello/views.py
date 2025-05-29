from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def juliano(request):
    return HttpResponse("Hello, Juliano!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
