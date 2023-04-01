from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class RegEvent(models.Model):
    intern = models.ForeignKey("extended_user.Profile", verbose_name="Студент", on_delete=models.RESTRICT,
                               related_name="regs_by_student")
    event_id = models.ForeignKey("event.Event", verbose_name="Мероприятие", on_delete=models.RESTRICT,
                                 related_name="regs_by_event")
    rating = models.IntegerField("Обратная связь", null=True, blank=True, validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(5)])
    estimation = models.IntegerField("Оценка работы студента", null=True, blank=True, validators=[MinValueValidator(0),
                                                                                                  MaxValueValidator(5)])
