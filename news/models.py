from django.db import models
from django.utils import timezone

# Create your models here.


class News(models.Model):
    title = models.CharField("Название новости", max_length=200)
    info = models.CharField("Описание", max_length=5000)
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата измения", default=timezone.now)
    author = models.ForeignKey("extended_user.Profile", verbose_name="Организаторы", on_delete=models.RESTRICT)
    photo = models.ImageField(verbose_name="Фото новости", blank=True, null=True, upload_to='media/')

    def __str__(self):
        return self.title
