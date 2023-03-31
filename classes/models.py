from django.db import models
from django.utils import timezone


# Create your models here.
class Class(models.Model):
    title = models.CharField("Название занятия", max_length=200)
    info = models.CharField("Описание", max_length=5000)
    event_id = models.ForeignKey("event.Event", verbose_name="Мероприятие", on_delete=models.RESTRICT,
                                 related_name="classes_by_event")
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата создания", default=timezone.now)
    start_date = models.DateField("Дата начала", blank=True, null=True)
    end_date_soft = models.DateField("Мягкий дедлайн", blank=True, null=True)
    end_date_hard = models.DateField("Жесткий дедлайн", blank=True, null=True)
    teacher = models.ForeignKey("extended_user.Profile", verbose_name="Преподаватель", on_delete=models.RESTRICT,
                               related_name='teacher')
    file = models.FileField(verbose_name="Прикрепленный файл", blank=True, null=True, upload_to='media/')

    def get_file_name(self):
        if self.file:
            return self.file.name.split("/")[-1]
        else:
            return None

    def __str__(self):
        return self.title
