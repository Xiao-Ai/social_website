from django.db import models
from django.forms import ModelForm

from account.models import User, Info
# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField()
    picture = models.ImageField(blank=True, upload_to="img/status_pic/")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.user.email


class StatusForm(ModelForm):
    class Meta:
        model = Status