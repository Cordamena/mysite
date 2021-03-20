from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Create your views here.

from .models import Question, Choice


# def index(request):
#     questions = Question.objects.all()

#     context = {
#         "questions" : questions
#     }
#     return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.all()


# def detail(request, q_id):
#     question = Question.objects.get(pk=q_id)
#     # choices = question.choice_set.all()
#     context = {
#         "question" : question
#     }
#     return render(request, "polls/detail.html", context )


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    

# def results(request, q_id):
#     question = Question.objects.get(pk=q_id)
#     context = {
#         "question" : question
#     }
#     return render(request, "polls/results.html", context )
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    

def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)


    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()

    return HttpResponseRedirect( reverse("polls:results", args=(q_id, )) )
