from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import strftime


# Create your models here.
class HomeWork(models.Model):
    info = models.TextField("Описание")
    classes_id = models.ForeignKey("classes.Class", verbose_name="Занятие", on_delete=models.RESTRICT,
                                   related_name="homeworks_by_classes")
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата редактирования", default=timezone.now)
    student_id = models.ForeignKey("extended_user.Profile", verbose_name="Студент", on_delete=models.RESTRICT,
                                   related_name='homeworks_by_student')
    file = models.FileField(verbose_name="Прикрепленный файл", blank=True, null=True, upload_to='media/')
    mark = models.IntegerField("Оценка", blank=True, null=True)
    comment = models.TextField("Комментарий от проверяющего", blank=True, null=True)

    def __str__(self):
        dt = self.time_edit.strftime("%d.%m.%Y, %H:%M:%S")
        return f"{self.student_id} от {dt}"


    def get_file_name(self):
        if self.file:
            return self.file.name.split("/")[-1]
        else:
            return None
