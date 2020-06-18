from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Project
from .forms import ContactForm



class HomePageView(View):
    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(self.request, 'home.html', context, status=200)


class AboutView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, 'about.html', context, status=200)


class ProjectListView(ListView):
    model = Project
    paginate_by = 9
    template_name = 'projects.html'


class SocialMediaView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, 'social-media.html', context, status=200)


class ContactView(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(self.request, 'contact.html', context, status=200)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = f"{name} ({email}, {phone}) says: {form.cleaned_data['message']}"
            try:
                send_mail(subject, message, email, ['jsharris.portfolio@gmail.com'])
                messages.success(self.request, "Your message has been sent")
                return redirect("core:contact")
            except BadHeaderError:
                messages.error(self.request, "Invalid header found. Try again.")
                return redirect("core:contact")
            except Exception as e:
                messages.error(self.request, "Something went wrong. Please try again.")
                return redirect("core:contact")
