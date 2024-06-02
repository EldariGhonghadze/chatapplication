from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from chat.models import Question
from chat.forms import QuestionCreateForm



def home_view(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'home.html',
        {
            'questions': Question.objects.all()
        }
    )

def question_create_view(request: HttpRequest) -> HttpResponse:
    form = QuestionCreateForm()
    if request.method == 'POST':
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    
    print(f'METHOD: {request.method}')
    print(f'POST: {request.POST}')
    print(f'GET: {request.GET}')
    return render(
        request,
        'question_create.html',
        {
            'form': form
        }
    )


class HomeView(ListView):
    model = Question
    template_name = 'home.html'
    context_object_name = 'questions'
    paginate_by = 25


class QuestionCreateView(CreateView):
    model = Question
    fields = '__all__'
    template_name = 'question_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.text += "Changed text"
        self.object.save()
        print(self.object.text)
        return redirect(self.success_url)


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'question_delete.html'
    success_url = reverse_lazy('home')


class QuestionUpdateView(UpdateView):
    model = Question
    fields = '__all__'
    template_name = 'question_create.html'

    def get_success_url(self) -> str:
        return reverse('question-detail', kwargs={'pk': self.object.pk})
