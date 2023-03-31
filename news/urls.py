from django.urls import path

from news.views import *

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
    path('news/', all_news, name='all_news'),
    path('news/<int:news_id>/', detail, name='detail'),
]