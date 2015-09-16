from django.db import models
from django.forms import ModelForm
from account.models import User
# Create your models here.
    
class Education(models.Model):
    user = models.OneToOneField(User)
    BACHELOR = 'Bachelor'
    MASTER = 'Master'
    DOCTOR = 'Doctor'
    
    DEGREE_CHOICES = (
                      (BACHELOR, 'Bachelor'),
                      (MASTER, 'Master'),
                      (DOCTOR, 'Doctor'),
                      )
    
    degree = models.CharField(max_length=8, choices=DEGREE_CHOICES, default=BACHELOR, blank=True)
    school = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.user.email
    

class Experience(models.Model):
    user = models.OneToOneField(User)
    activity = models.TextField(blank=True)
    internship = models.TextField(blank=True)
    awards = models.TextField(blank=True)
    association = models.TextField(blank=True)
    other = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.user.email

class EducationForm(ModelForm):
    class Meta:
        model = Education

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

