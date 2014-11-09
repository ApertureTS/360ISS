from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Drinker(models.Model):
    user    = models.OneToOneField(User)
    name    = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    def __str__(self):
    	return unicode(self).encode('utf-8')    

