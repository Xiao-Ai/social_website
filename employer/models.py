from django.db import models
from django.forms import ModelForm
from account.models import User

# Create your models here.
class Employer(models.Model):
    corporation = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=18)
 
    def __unicode__(self):
        return self.email

class Job(models.Model):
    employer = models.ForeignKey(Employer)
    applicants = models.ManyToManyField(User, blank=True, related_name="applicants", symmetrical=False)
    employees = models.ManyToManyField(User, blank=True, related_name="employees", symmetrical=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    requirement = models.TextField()
    address = models.TextField()
    others = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = ['corporation', 'email', 'password']

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [ 'title', 'description', 'requirement', 'address', 'others']