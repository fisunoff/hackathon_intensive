from django.db import models


# Create your models here.


class RegEvent(models.Model):

    intern = models.ForeignKey("extended_user.Profile", verbose_name="Студент", on_delete=models.RESTRICT)
    event_id = models.ForeignKey("event.Event", verbose_name="Мероприятие", on_delete=models.RESTRICT)
    rating = models.IntegerField("Оценка мероприятия со стороны студента", null=True, blank=True)
    estimation = models.IntegerField("Оценка работы студента", null=True, blank=True)
