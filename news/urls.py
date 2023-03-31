from django.urls import path

from news.views import *

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
    # path('news/', all_news, name='all_news'),
    # path('news/<int:news_id>/', detail, name='detail'),
    path('news/', NewsListView.as_view(), name='home'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='post_detail'),
    path('post/new/', NewsCreatView.as_view(), name='post_new'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='post_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='post_delete'),
]