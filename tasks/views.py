from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('welcome to the world')
def contact(request):
    return HttpResponse("<h2 style='color:green'>this is the contact page</h2>")
def showtask(request):
    return HttpResponse("show your task")