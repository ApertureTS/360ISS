from django.db import models


#from dragdrop.files import get_path
from dragdrop.views import content_file_name
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.cached_db import SessionStore
from drinker.models import Drinker

# Create your models here.
def __str__(self):
    return unicode(self).encode('utf-8')
#class UploadFile(models.Model):
	#print "****views.a_user:%s" % views.a_user


    # uses python's strfttime() function
    # https://docs.python.org/3/library/time.html#time.strftime 
    # this gets stored to the static -> media file
    # file = models.FileField(upload_to='files/%Y/%m/%d')
 	#
 	# from:
 	# http://joshourisman.com/2008/11/18/dynamic-upload-path-django-filefieldimagefield/
 	# this uses the import from forms.py to use the function get_path which is
 	# customizable and dynamic to the user
 	# file = models.FileField(upload_to=get_path)
 	
 	# debugging statements
 	# print "UploadFile is being accessed"
 	# print "this is User: %s" % User
 	
 	# this will cause problems
 	# the "User" is a string so IntegerField and TextField works either or
 	# user = models.IntegerField(User)
 	# user = models.TextField(User)
 	 
 	# does not cause any problems when "User" is in the parameter
 	# Finally, note a relationship is defined, using ForeignKey. That tells 
 	# Django each UploadFile is related to a single User. Django supports all 
 	# the common database relationships: many-to-one, many-to-many and one-to-one.
 	# 
 	# This is a many-to-one relationship, where the images are multi-uploaded on
 	# the client-side 
 	# 
 	# when the line "user = models.ForeignKey(User)" it does not upload the
 	# images in the site folder, then how would you be able to 
 	# many-to-one relationship
	#class UserUpload(models.Model):
	#user = models.ForeignKey(User)
 	#user = models.ForeignKey(User, unique=True)
	#my_path=str(user)

 	#print "*****this is str(user)  %s " % (my_path)

 #	print Drinker.objects.all()
  
  #a_path= temp_name
 	#print "path for cur_user %s" %  cur_user
  
  #self.Usr_name.temp_name# a_path#(cur_user)
 	
  # so should the upload be done with the "user" parameter passed into the
 	# upload_to?
 	#file = models.FileField(upload_to='home')

#class Usr_name(models.Model):
 # temp_name = models.CharField(max_length=128)
#  print Usr_name.objects.all()

# class UploadFile(models.Model):
#     user = models.OneToOneField(User)
#     print "path for cur_user %s" %  str(user.username)

#     file = models.FileField(upload_to=file)

# def file(self, filename):
#     url = "files/users/%s/%s" % (self.user.username, filename)
#     print "path for cur_user %s" %  str(self.user.username)
#     return url

# def content_file_name(instance, filename):
#     print "**-**username %s" % instance.user.username
#     return '/'.join(['content', instance.user.username, filename])

def content_file_name(instance, filename):
    print "**-**def username %s" % instance.user.username
    return '/'.join(['content', instance.user.username, filename])    

class UploadFile(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    print "**-**class username %s" % user
    file = models.FileField(upload_to=content_file_name) 
