from django.db import models
from django.forms import ModelForm

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=18)
    friends = models.ManyToManyField('self', null=True, blank=True, symmetrical=False)
    
    def __unicode__(self):
        return self.email
    
    def _get_full_name(self):
        return '%s%s' % (self.last_name, self.first_name)
    
    full_name = property(_get_full_name)

class Info(models.Model):
    email = models.OneToOneField(User)
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = (
                      (MALE,'Male'), 
                      (FEMALE,'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)
    
    pic = models.ImageField(upload_to='img/account_pic/')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    age = models.IntegerField(default=0)
    major = models.CharField(max_length=100, blank=True)
    profile = models.TextField(blank=True)
    def __unicode__(self):
        return unicode(self.email)

class UserForm(ModelForm):
    class Meta:
        model = User

class InfoForm(ModelForm):
    class Meta:
        model = Info
