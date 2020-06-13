from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.generic import View, ListView, DetailView
from .models import Project
from .forms import ContactForm


class HomePageView(View):
    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(self.request, 'home.html', context, status=200)
