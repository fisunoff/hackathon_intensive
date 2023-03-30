from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    title = models.CharField("Название мероприятия", max_length=200)
    info = models.CharField("Описание", max_length=5000)
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата создания", default=timezone.now)
    registration_start = models.DateTimeField("Начало регистрации", default=timezone.now, blank=True, null=True)
    registration_end = models.DateTimeField("Конец регистрации", blank=True, null=True)
    start_date = models.DateField("Дата начала", blank=True, null=True)
    end_date = models.DateField("Дата окончания", blank=True, null=True)
    author = models.ForeignKey("extended_user.Profile", verbose_name="Организаторы", on_delete=models.RESTRICT)
    file = models.FileField(verbose_name="Прикрепленный файл", blank=True, null=True, upload_to='media/')

    @property
    def is_register_date(self):
        if timezone.now() >= self.registration_start:
            if (not self.registration_end) or (self.registration_end >= timezone.now()):
                return True
        return False
