from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from funcs import group_required
# Create your views here.

from reg_event.tables import RegEventTable

from reg_event.models import RegEvent


class RegEventListView(SingleTableView):
    model = RegEvent
    template_name = 'reg_event/list.html'
    table_class = RegEventTable

    def get_queryset(self):
        return RegEvent.objects.filter(event_id=self.request.GET.get('event_id'))


class RegEventCreate(CreateView):
    model = RegEvent
    template_name = 'reg_event/create.html'
    success_url = reverse_lazy('event-list')

    fields = ('intern', 'event_id')

    def get_initial(self):
        initial_data = {}
        for i in ['intern', 'event_id']:
            initial_data[i] = self.request.GET.get(i)
        return initial_data


class RegEventDetail(DetailView):
    model = RegEvent
    template_name = 'reg_event/detail.html'
    context_object_name = 'reg_event'

    def get_context_data(self, **kwargs):
        context = super(RegEventDetail, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        context['is_staff'] = user.groups.filter(name__in=['worker', ]).exists()
        return context


class RegEventStudentUpdate(UpdateView):
    model = RegEvent
    template_name = 'reg_event/update.html'

    fields = ('rating', )

    def get_initial(self):
        initial_data = {}
        for i in ['intern', 'event_id']:
            initial_data[i] = self.request.GET.get(i)
        return initial_data

    def get_success_url(self):
        return reverse_lazy('event-detail', kwargs={'pk': self.object.event_id.id})


class RegEventStaffUpdate(UpdateView):
    model = RegEvent
    template_name = 'reg_event/update.html'

    fields = ('estimation', )

    def get_initial(self):
        initial_data = {}
        for i in ['intern', 'event_id']:
            initial_data[i] = self.request.GET.get(i)
        return initial_data

    def get_success_url(self):
        return reverse_lazy('event-detail', kwargs={'pk': self.object.event_id.id})
