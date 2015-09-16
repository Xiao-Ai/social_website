from django.contrib import admin

# Register your models here.
from models import Employer, Job

class EmployerAdmin(admin.ModelAdmin):
    list_display = ['corporation', 'email']
    class Meta:
        model = Employer

class JobAdmin(admin.ModelAdmin):
    list_display = ['employer', 'title', 'timestamp']
    class Meta:
        model = Job

admin.site.register(Employer, EmployerAdmin)
admin.site.register(Job, JobAdmin)
