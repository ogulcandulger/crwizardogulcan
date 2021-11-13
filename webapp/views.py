from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth import (
    get_user_model
)

User = get_user_model()

from_email = 'Cr Wizard Ogulcan Dulger <crwizardogulcan@gmail.com>'

def custom_page_not_found_view(request, exception):
    return redirect('/')

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'