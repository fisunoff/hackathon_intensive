from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from funcs import group_required
# Create your views here.

from classes.tables import ClassesTable

from classes.models import Class
from homework.models import HomeWork


class ClassesListView(SingleTableView):
    model = Class
    template_name = 'classes/list.html'
    table_class = ClassesTable

    def get_queryset(self):
        return Class.objects.filter(event_id=self.request.GET.get('event_id'))


class ClassesCreateView(CreateView):
    model = Class
    template_name = 'event/create.html'
    fields = ('title', 'info', 'start_date', 'event_id',
              'end_date_soft', 'end_date_hard', 'teacher', 'file')
    success_url = reverse_lazy('event-list')

    def get_initial(self):
        initial_data = {}
        for i in ('title', 'info', 'start_date', 'event_id',
                  'end_date_soft', 'end_date_hard', 'teacher', 'file'):
            initial_data[i] = self.request.GET.get(i)
        return initial_data


class ClassesDetailView(DetailView):
    model = Class
    template_name = 'classes/detail.html'
    context_object_name = 'classes'

    """def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['filename'] = self.object.get_file_name()
        tags = ",".join([str(i.id) for i in self.object.tags.all()])
        context['to_copy'] = f"?interaction_name={self.object.interaction_name}&description={self.object.description}" \
                             f"&type={self.object.type.id if self.object.type else None}" \
                             f"&mentor={self.object.mentor.id if self.object.mentor else None}" \
                             f"&student={self.object.student.id if self.object.student else None}" \
                             f"&start_date={self.object.start_date}&end_date={self.object.end_date}" \
                             f"&status={self.object.status.id if self.object.status else None}" \
                             f"&tags={tags}"
        return context"""

    # копирование. пока не делаем

    def get_context_data(self, **kwargs):
        context = super(ClassesDetailView, self).get_context_data(**kwargs)
        context['filename'] = self.object.get_file_name()
        user = User.objects.get(pk=self.request.user.id)
        context['is_staff'] = user.groups.filter(name__in=['worker', ]).exists()
        context['link_to_event'] = f"?event_id={self.object.pk}"
        context['link_to_add_homework'] = f"?classes_id={self.object.pk}&student_id={self.request.user.profile.id}"
        context['homeworks'] = HomeWork.objects.filter(student_id=self.request.user.profile.id,
                                                       classes_id=self.object.id).all()
        return context


class ClassesDeleteView(DeleteView):
    model = Class
    template_name = 'classes/delete.html'
    success_url = reverse_lazy('event-list')


class ClassesUpdateView(UpdateView):
    model = Class
    template_name = 'classes/update.html'
    context_object_name = 'classes'
    fields = ('title', 'info', 'start_date',
              'end_date_soft', 'end_date_hard', 'teacher', 'file')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('event-detail', kwargs={'pk': self.object.id})
