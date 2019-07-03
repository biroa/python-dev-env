from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# In that case if we like to use loader instead of render
#from django.template import loader

def index(request):
    # Order pud_date -> but pub date in reverse order -pud_date
    # [:5] -> limit fie -> 0,1,2,3,4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # this is list comprehension -> [q.question_text for q in latest_question_list]
    output = ', '.join([q.question_text for q in latest_question_list])

    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse( template.render(context, request) )
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    #
    # the get_object_or_404 provide the same output as the code above

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
      # We try to get the object from the server with try/catch shortcut
      question = get_object_or_404(Question, pk=question_id)
      try:
          # request.POST is a dictiopnary
          selected_choice = question.choice_set.get(pk=request.POST['choice']);
      # raise KeyError when the key is not in the dictionary
      except(KeyError, Choice.DoesNotExist):
          # Redisplay questions detail choice
          return render(request, 'polls/detail.html',{'question':question,
            'error_message':"You did not select a choice",
          })
      else:
          selected_choice.votes += 1
          selected_choice.save()

          return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
