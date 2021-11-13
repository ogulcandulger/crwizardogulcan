from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.views.generic import TemplateView, ListView, DetailView, View
from django.conf import settings
from django.contrib import messages
import requests
from urllib.request import urlopen
from django.views.decorators.http import require_http_methods
from django.db.models.signals import post_save
from django.dispatch import receiver
from collections import OrderedDict
import lxml
import lxml.etree
import xmltodict
import xml.etree.ElementTree as ET
import os
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (
    get_user_model
)

from .forms import (
    XMLForm 
)

User = get_user_model()

from_email = 'CRWizard Ogulcan Dulger <crwizardogulcan@gmail.com>'

def custom_page_not_found_view(request, exception):
    return redirect('/')


def listRecursive (d, key, path = None):
    if not path: path = []
    for k, v in d.items ():
        if isinstance (v, OrderedDict):
            for path, found in listRecursive (v, key, path + [k] ):
                yield path, found
        if k == key:
            yield path + [k], v

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

    #Get XML model form
    def get(self, *args, **kwargs):
        try:
            form = XMLForm()
            context = {
                'form': form,
                'media_url':settings.MEDIA_URL, 
                'static_url':settings.STATIC_URL
            }
            return render(self.request, "homepage.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "Please try again!")
            return redirect("/")

    def post(self, request, *args, **kwargs):
        try:
            form = XMLForm(self.request.POST)
            xml_link = form[('xml_link')].value()
            word = form[('word')].value()
            if form.is_valid():
                toEmail = self.request.user.email
                try: 
                    response = requests.get(xml_link)
                    data = xmltodict.parse(response.content)
                    listRecursive (data, 'PLANT')
                    #This function should be replacing the words, but not at the moment , instead I save it directly

                    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/xml_file.xml'), 'wb') as f:
                        f.write(response.content)
                    
                    xml = form.save(commit=False)
                    xml.user = self.request.user
                    xml.xml_file = 'xml_file.xml'
                    xml.word = word
                    xml.save()
                except:
                    message = 'Invalid XML file, please try again!'
                    send_mail(
                        'Warning! Invalid XML file',
                        message,
                        from_email,
                        [toEmail],
                        fail_silently=False,
                    )
                messages.success(self.request, "We got your XML link!")
                return redirect("/")
            else:
                messages.warning(self.request, "Please try again!")
                return redirect("/")
        except ObjectDoesNotExist:
            messages.info(self.request, "Please try again!")
            return redirect("/")