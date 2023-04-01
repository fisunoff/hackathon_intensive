from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

from event.tables import EventTable

from event.models import Event
from reg_event.models import RegEvent

class EventListView(SingleTableView):
    model = Event
    template_name = 'event/list.html'
    table_class = EventTable

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = User.objects.get(pk=self.request.user.id)
            context['is_staff'] = user.groups.filter(name__in=['worker', ]).exists()
        else:
            context['is_staff'] = False
        return context


@method_decorator(login_required, name='dispatch')
class EventCreateView(CreateView):
    model = Event
    template_name = 'event/create.html'
    fields = ('title', 'info', 'registration_start', 'registration_end',
              'start_date', 'end_date', 'author', 'organizers', 'file')
    success_url = reverse_lazy('event-list')

    def get_initial(self):
        initial_data = {}
        for i in ['interaction_name', 'student', 'description', 'type', 'mentor', 'start_date', 'end_date',
                  'status', 'tags']:
            initial_data[i] = self.request.GET.get(i)
        tags_request = self.request.GET.get('tags')
        if tags_request:
            initial_data['tags'] = list(map(int, self.request.GET.get('tags').split(",")))
        return initial_data


@method_decorator(login_required, name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'event/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['filename'] = self.object.get_file_name()
        user = User.objects.get(pk=self.request.user.id)
        context['is_staff'] = user.groups.filter(name__in=['worker', ]).exists()
        context['link'] = f"?event_id={self.object.pk}"
        context['students_count'] = len(self.object.regs_by_event.all())
        context['classes_count'] = len(self.object.classes_by_event.all())
        context['is_student_registered'] = RegEvent.objects.filter(intern=user.id, event_id=self.object.pk).first()
        c = 0
        summ = 0
        for reg in self.object.regs_by_event.all():
            if reg.rating:
                c += 1
                summ += reg.rating
        if c > 0:
            context['avarage_rating'] = str(summ / c)
        else:
            context['avarage_rating'] = "Нет оценок"
        context['link_to_new_classes'] = f"?event_id={self.object.pk}&teacher={self.request.user.profile.id}"
        context['link_to_classes'] = f"?event_id={self.object.pk}"
        if self.request.user.id:
            context['link_to_reg'] = f"?intern={self.request.user.profile.id}&event_id={self.object.pk}"
        return context


@method_decorator(login_required, name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event/delete.html'
    success_url = reverse_lazy('event-list')


@method_decorator(login_required, name='dispatch')
class EventUpdateView(UpdateView):

    model = Event
    template_name = 'event/update.html'
    context_object_name = 'event'
    fields = ('title', 'info', 'registration_start', 'registration_end',
              'start_date', 'end_date', 'author', 'organizers', 'file')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('event-detail', kwargs={'pk': self.object.id})