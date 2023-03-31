from django.contrib.auth.models import User
from django.db import models
from news.models import News


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField("Описание комментария")
    time_creat = models.DateTimeField("Дата создания", auto_now_add=True)
    time_edit = models.DateTimeField("Дата измения", auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
