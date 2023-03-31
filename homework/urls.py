from django.urls import path, include

from homework.views import *

urlpatterns = [
    path('', HomeWorkListView.as_view(), name="homework-list"),
    path('create/', HomeWorkCreateView.as_view(), name='homework-create'),
    path('<int:pk>/', HomeWorkDetailView.as_view(), name='homework-detail'),
    path('<int:pk>/update/', HomeWorkUpdateByStudentView.as_view(), name='homework-update'),
    path('<int:pk>/rate/', HomeWorkUpdateByStaffView.as_view(), name='homework-rate'),
    path('<int:pk>/delete/', HomeWorkDeleteView.as_view(), name='homework-delete'),

]
