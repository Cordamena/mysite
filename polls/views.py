from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question
    }
    return render(request, "polls/results.html", context )
    

def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)

    res = ""
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()

    return HttpResponseRedirect( reverse("polls:results", args=(q_id, )) )
