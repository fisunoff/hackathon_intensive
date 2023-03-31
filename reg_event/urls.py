from django.urls import path, include

from reg_event.views import *

urlpatterns = [
    path('', RegEventListView.as_view(), name="reg_event-list"),
    path('create/', RegEventCreate.as_view(), name='reg_event-create'),
    path('<int:pk>/', RegEventListView.as_view(), name='reg_event-detail'),
    path('<int:pk>/update/', RegEventListView.as_view(), name='reg_event-update'),
    path('<int:pk>/delete/', RegEventListView.as_view(), name='reg_event-delete'),

]
