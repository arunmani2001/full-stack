from django import forms
from .models import RTCRecord

class RTCUploadForm(forms.ModelForm):
    class Meta:
        model = RTCRecord
        fields = ['document']