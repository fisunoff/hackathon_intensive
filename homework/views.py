from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from funcs import group_required
# Create your views here.

from homework.tables import HomeWorkTable

from homework.models import HomeWork


class HomeWorkListView(SingleTableView):
    model = HomeWork
    template_name = 'homework/list.html'
    table_class = HomeWorkTable

    def get_queryset(self):
        classes_id = self.request.GET.get('classes_id')
        student_id = self.request.GET.get('student_id')
        if classes_id and student_id:
            return HomeWork.objects.filter(classes_id=classes_id, student_id=student_id)
        elif classes_id:
            return HomeWork.objects.filter(classes_id=classes_id)
        elif student_id:
            return HomeWork.objects.filter(student_id=student_id)
        return HomeWork.objects.all()


class HomeWorkCreateView(CreateView):
    model = HomeWork
    template_name = 'homework/create.html'
    fields = ('info', 'classes_id', 'student_id', 'file')
    success_url = reverse_lazy('event-list')

    def get_initial(self):
        initial_data = {}
        for i in ['classes_id', 'student_id']:
            initial_data[i] = self.request.GET.get(i)
        return initial_data


class HomeWorkDetailView(DetailView):
    model = HomeWork
    template_name = 'homework/detail.html'
    context_object_name = 'homework'

    def get_context_data(self, **kwargs):
        context = super(HomeWorkDetailView, self).get_context_data(**kwargs)
        context['filename'] = self.object.get_file_name()
        user = User.objects.get(pk=self.request.user.id)
        context['is_staff'] = user.groups.filter(name__in=['worker', ]).exists()
        return context


class HomeWorkDeleteView(DeleteView):
    model = HomeWork
    template_name = 'homework/delete.html'
    success_url = reverse_lazy('event-list')


class HomeWorkUpdateByStudentView(UpdateView):
    model = HomeWork
    template_name = 'homework/update.html'
    context_object_name = 'homework'
    fields = ('info', 'file')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('homework-detail', kwargs={'pk': self.object.id})


class HomeWorkUpdateByStaffView(UpdateView):
    model = HomeWork
    template_name = 'homework/update.html'
    context_object_name = 'homework'
    fields = ('mark', 'comment')

    def get_success_url(self):
        print("succes типа")
        return reverse_lazy('homework-detail', kwargs={'pk': self.object.id})