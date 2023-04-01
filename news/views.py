from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView , ListView

from news.models import News


def home(request: HttpRequest):
    return redirect('news/')


class NewsListView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = User.objects.get(pk=self.request.user.id)
            context['is_staff'] = user.groups.filter(name__in=['worker', ]).exists()
        else:
            context['is_staff'] = False
        return context

class NewsCreatView(CreateView):
    model = News
    template_name = 'news/new.html'
    fields = ['title', 'author', 'info', 'photo']


class NewsUpdateView(UpdateView):
    models = News
    template_name = 'news/edit.html'
    fields = ('title', 'info', 'time_create', 'author', 'photo')

    def get_queryset(self):
        return News.objects.all()


class NewsDeleteView(DeleteView):  # Создание нового класса
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy('news:home')