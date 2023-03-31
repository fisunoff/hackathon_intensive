import django_tables2 as tables
from classes.models import Class


class HomeWorkTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'homework-detail\' record.id %}">&#128203;</a>', orderable=False,
                                 verbose_name="")

    class Meta:
        model = Class
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'student_id', 'time_edit', 'mark')
