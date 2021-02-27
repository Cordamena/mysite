from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Question, Choice


def index(request):
    q_all = Question.objects.all()
    res = "<ol>"
    for g in q_all:
        res += "<li>%s</li>" % g.text
    res += "</ol>"

    return HttpResponse(res)

def meme(request):
    return HttpResponse("<img src='https://management30.com/wp-content/uploads/2016/03/change-management-dead.jpg'>")

def detail(request, q_id):
    res = "Question number %s." % q_id
    return HttpResponse(res)

def results(request, q_id):
    res = "Result fot Question number %s." % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote fot Question number %s." % q_id
    return HttpResponse(res)
