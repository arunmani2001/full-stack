from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
class RTCRecord(models.Model):
    survey_number = models.IntegerField(default="")
    surnoc = models.CharField(max_length=10, blank=True, null=True)
    hissa = models.IntegerField(default="")
    village = models.CharField(max_length=100)
    hobli = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    owner_name = models.TextField(default="")
    document = models.FileField(upload_to='rtcs/')
    extracted = models.BooleanField(default=False)
    # period = models.DateTimeField(null=True, blank=True)