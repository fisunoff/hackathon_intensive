from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from news.models import News


def home(request: HttpRequest):
    return redirect('news/')


def all_news(request: HttpRequest):
    news = News.objects.order_by('-time_create')
    context = {
        'news': news,
    }
    return render(request, 'news/home.html', context=context)


def detail(request: HttpRequest, news_id: int):
    news = get_object_or_404(News, pk=news_id)
    context = {
        'news': news,
    }
    return render(request, 'news/detail.html', context=context)
