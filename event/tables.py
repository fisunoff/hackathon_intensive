import django_tables2 as tables
from event.models import Event


class EventTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'event-detail\' record.id %}">&#128203;</a>', orderable=False,
                                 verbose_name="")

    class Meta:
        model = Event
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'title', 'registration_start', 'registration_end', 'start_date', 'end_date')
