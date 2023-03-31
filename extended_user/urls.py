from django.urls import path

from extended_user.views import *

urlpatterns = [
    path('', SignUp.as_view(), name='register')
]