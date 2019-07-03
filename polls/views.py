from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Generic View Classes usage in Django

class IndexView(generic.ListView):
    # template_name: Django specific variable without this it will not work
    template_name = 'polls/index.html' # the used name of a template
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the latest five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
