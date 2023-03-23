from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest, HttpResponse

from polls.models import Question

def _get_question_by_id(question_id: int) -> Question | Http404:
    return get_object_or_404(Question, pk=question_id)

def index(request: HttpRequest) -> HttpResponse:
    try:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    except Exception as err:
        raise Http404('Cannot retrieve question list') from err
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return render(request, 'polls/detail.html', {'question': _get_question_by_id(question_id)})

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return render(request, 'polls/results.html', {'question': _get_question_by_id(question_id)})

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return render(request, 'polls/vote.html', {'question': _get_question_by_id(question_id)})