from django.urls import path, include
from .views import (
    HomePageView,
    AboutView,
    ProjectListView,
    SocialMediaView,
    ContactView,
    TestView, 
)


app_name = 'core'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('social-media/', SocialMediaView.as_view(), name='social'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('test/', TestView.as_view(), name='test'),
]