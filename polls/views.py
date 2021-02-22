from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>With great power comes great responsobility<h1>")

def meme(request):
    return HttpResponse("<img src='https://management30.com/wp-content/uploads/2016/03/change-management-dead.jpg'>")