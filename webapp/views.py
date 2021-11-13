from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.views.generic import TemplateView, ListView, DetailView, View
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (
    get_user_model
)

from .forms import (
    XMLForm 
)

User = get_user_model()

from_email = 'Cr Wizard Ogulcan Dulger <crwizardogulcan@gmail.com>'

def custom_page_not_found_view(request, exception):
    return redirect('/')

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

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
            if form.is_valid():
                user = self.request.user.email
                print(user)
                print(xml_link)
                # message = name  +', ' + 'mesaj gönderdi.' + '\n\n'+ 'Firma Ünvanı: ' + company + '\n\n'+ 'Faaliyet Gösterilen İş Alanı: ' + company_subject + '\n\n'+ 'Yaş: ' + age + '\n\n'+ 'Telefon Numarası: ' + number + '\n\n' + 'E-Posta: ' + email + '\n\n'+ 'Şehir: ' + city + '\n\n'+ 'İlçe: ' + province + '\n\n'+  'Mesaj: ' +  message
                # send_mail(
                #     'Baibars Bayilik Mesajı',
                #     message,
                #     from_email,
                #     ['ogulcan.dulger@gmail.com'],
                #     fail_silently=False,
                # )
                # send_mail(
                #     'Baibars Bayilik Mesajı',
                #     message,
                #     from_email,
                #     ['info@baibars.com.tr'],
                #     fail_silently=False,
                # )
                messages.success(self.request, "We got your XML link!")
                return redirect("/")
            else:
                messages.warning(self.request, "Please try again!")
                return redirect("/")
        except ObjectDoesNotExist:
            messages.info(self.request, "Lütfen tekrar deneyiniz!")
            return redirect("/")