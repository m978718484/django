from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
 
# Create your views here.

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  #output = ', '.join([q.question_text for q in latest_question_list])
  context = {
      'latest_question_list':latest_question_list,
  }
  return HttpResponse(template.render(context,request))


def detail(request,question_id):
  #try:
    #question = Question.objects.get(pk=question_id)
  #except Question.DoesNotExist:
    #raise Http404("Question does not exist")
  question = get_object_or_404(Question,pk=question_id)
  return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
  response = "you're looking at the results of question %s."
  return HttpResponse(response%question_id)

def vote(request,question_id):
  return HttpResponse("you're voting on question %s."%question_id)

