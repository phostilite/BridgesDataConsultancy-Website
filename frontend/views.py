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