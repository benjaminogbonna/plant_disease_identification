from dataclasses import fields
from tkinter import Image
from django import forms
from .models import Image


# class Upload(forms.Form):
#     image = forms.ImageField(label='Choose Image')

class Upload(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        