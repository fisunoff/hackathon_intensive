from django.db import models


# Create your models here.


class RegEvent(models.Model):
    marks = (1, 2, 3, 4, 5)

    intern = models.ForeignKey("extended_user.Profile", "Студент", on_delete=models.RESTRICT)
    event_id = models.ForeignKey("event.Event", "Мероприятие", on_delete=models.RESTRICT)
    rating = models.IntegerField("Оценка мероприятия со стороны студента", null=True, blank=True, choices=marks)
    estimation = models.IntegerField("Оценка работы студента", null=True, blank=True, choices=marks)
