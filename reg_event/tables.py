import django_tables2 as tables
from reg_event.models import RegEvent


class RegEventTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'profile-detail\' record.intern.id %}">&#128203;</a>',
                                 orderable=False, verbose_name="")

    class Meta:
        model = RegEvent
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'intern', 'rating')
