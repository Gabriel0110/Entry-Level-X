from django.contrib import admin
from job_search.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobAdmin)