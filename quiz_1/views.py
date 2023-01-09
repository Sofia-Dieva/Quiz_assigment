from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Answer, Question, Quiz
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def welcome_page(request):
    return render(request, 'quiz_1/main_page.html')


class QuizDetail(DetailView):
    model = Quiz
    template_name = 'quiz_1/quiz_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'quiz'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context['all_answers_and_questions'] = {}
        context['right_answers'] = {}
        for item in Question.objects.filter(quiz__pk=pk):
            context['all_answers_and_questions'][item] = Answer.objects.filter(where=item)
            context['right_answers'][item] = item.Answers.filter(is_right_answer=True)
        return context


class QuizListView(ListView):
    template_name = "quiz_1/all.html"
    model = Quiz
    context_object_name = "all_quizzes"
