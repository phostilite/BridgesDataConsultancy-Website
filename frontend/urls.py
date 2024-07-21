from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('services/', views.services_view, name='services'),
    path('get-started/', views.get_started_view, name='get_started'),
    path('carrers/', views.carrers_view, name='carrers'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('case-studies/', views.case_studies_view, name='case_studies'),
    path('schedule-consultation/', views.schedule_consultation_view, name='schedule_consultation'),
]