from django.http import HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.conf import settings

def home_view(request):
    try:
        return render(request, settings.HOME_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Home page template does not exist.", status=404)

def about_view(request):
    try:
        return render(request, settings.ABOUT_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("About page template does not exist.", status=404)

def contact_view(request):
    try:
        return render(request, settings.CONTACT_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Contact page template does not exist.", status=404)

def services_view(request):
    try:
        return render(request, settings.SERVICES_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Services page template does not exist.", status=404)
    
def get_started_view(request):
    try:
        return render(request, settings.GET_STARTED_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Get Started page template does not exist.", status=404)
    
def carrers_view(request):
    try:
        return render(request, settings.CARRERS_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Carrers page template does not exist.", status=404)
    
def blogs_view(request):
    try:
        return render(request, settings.BLOGS_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Blogs page template does not exist.", status=404)
    
def case_studies_view(request):
    try:
        return render(request, settings.CASE_STUDIES_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Case Studies page template does not exist.", status=404)
    
def schedule_consultation_view(request):
    try:
        return render(request, settings.SCHEDULE_CONSULTATION_TEMPLATE)
    except TemplateDoesNotExist:
        return HttpResponse("Schedule Consultation page template does not exist.", status=404)