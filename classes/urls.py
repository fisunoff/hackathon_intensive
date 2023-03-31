from django.urls import path, include

from classes.views import *

urlpatterns = [
    path('', ClassesListView.as_view(), name="classes-list"),
    path('create/', ClassesCreateView.as_view(), name='classes-create'),
    path('<int:pk>/', ClassesDetailView.as_view(), name='classes-detail'),
    path('<int:pk>/update/', ClassesUpdateView.as_view(), name='classes-update'),
    path('<int:pk>/delete/', ClassesDeleteView.as_view(), name='classes-delete'),

]
