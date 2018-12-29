from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse('index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
    #return HttpResponse("You're asking for question %s" % question_id)


def result(request, question_id):
    return HttpResponse("You're asking for the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting for question %s" % question_id)
