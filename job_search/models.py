from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    description = HTMLField()
    company_url = models.CharField(max_length=256)