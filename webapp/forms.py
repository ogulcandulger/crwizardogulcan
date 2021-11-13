from django import forms
from django.forms import DateInput, TimeInput
from .models import (
    XML
)
from django.forms import ModelChoiceField

class XMLForm(forms.ModelForm):
    class Meta:
        model = XML
        fields = ["xml_link", "word"]