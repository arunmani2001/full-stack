from django.db import models

# Create your models here.
class RTCRecord(models.Model):
    survey_number = models.CharField(max_length=10)
    surnoc = models.CharField(max_length=10, blank=True, null=True)
    hissa = models.CharField(max_length=5)
    village = models.CharField(max_length=100)
    hobli = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    owner_name = models.TextField()
    document = models.FileField(upload_to='rtcs/')
    extracted = models.BooleanField(default=False)