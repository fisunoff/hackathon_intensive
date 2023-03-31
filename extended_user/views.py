from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# 1ый вариант
from django.urls import reverse_lazy
from django.views.generic import CreateView


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})


# 2ой вариант
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
