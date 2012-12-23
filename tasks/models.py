from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)


	def __unicode__(self):
		return self.user.username

class Project(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length = 200)
	date_created = models.DateTimeField('date created')

	def __unicode__(self):
		return self.user.username + ' - ' + self.name



class Task(models.Model):
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 1000, null=True, 
		blank=True)
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project, null=True, 
		blank=True)
	date_created = models.DateTimeField('date created')
	date_due = models.DateTimeField('date due', null=True, 
		blank=True)
	date_completed = models.DateTimeField('date completed', null=True, 
		blank=True)
	importance = models.IntegerField(null=True, 
		blank=True)
	completed = models.BooleanField(default = False)
	deleted = models.BooleanField(default = False)

	def __unicode__(self):
		return self.user.username + ' - ' + self.title






