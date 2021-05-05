from django import forms
from .models import *


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["number"]
