from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SingUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/sing_up.html'
    success_url = reverse_lazy('login')

