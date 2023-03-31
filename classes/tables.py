import django_tables2 as tables
from classes.models import Class


class ClassesTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'classes-detail\' record.id %}">&#128203;</a>', orderable=False,
                                 verbose_name="")

    class Meta:
        model = Class
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'title', 'start_date', 'end_date_soft', 'end_date_hard', 'teacher')
