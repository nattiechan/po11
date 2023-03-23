from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest, HttpResponse

from polls.models import Question

def index(request: HttpRequest) -> HttpResponse:
    try:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    except Exception as err:
        raise Http404('Cannot retrieve question list') from err
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question: Question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'You are looking at the results of question {question_id}.')

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'You are voting on question {question_id}.')