from django import forms
from .models import gamedata

class gameform(forms.ModelForm):
    class Meta:
        model=gamedata
        fields=['data',]