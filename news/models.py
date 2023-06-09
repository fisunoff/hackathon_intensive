from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class News(models.Model):
    title = models.CharField("Название новости", max_length=200)
    info = models.TextField("Описание")
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата измения", default=timezone.now)
    author = models.ForeignKey("extended_user.Profile", verbose_name="Автор", on_delete=models.RESTRICT)
    photo = models.ImageField(verbose_name="Фото новости", blank=True, null=True, upload_to='media/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post_detail', args=[str(self.id)])

    @property
    def info_short(self):
        if len(self.info) > 80:
            return self.info[:80] + "..."
        else:
            return self.info
