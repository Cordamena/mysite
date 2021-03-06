from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Question, Choice


def index(request):
    questions = Question.objects.all()

    context = {
        "questions" : questions
    }
    return render(request, "polls/index.html", context)


def meme(request):
    return HttpResponse("<img src='https://management30.com/wp-content/uploads/2016/03/change-management-dead.jpg'>")

def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    # choices = question.choice_set.all()
    context = {
        "question" : question
    }
    return render(request, "polls/detail.html", context )

def results(request, q_id):
    res = "Result fot Question number %s." % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote fot Question number %s." % q_id
    return HttpResponse(res)
