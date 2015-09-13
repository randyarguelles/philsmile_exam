from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Link(models.Model):
	url=models.URLField(unique=True)
	
class Bookmark(models.Model):
  title = models.CharField(max_length=200)
  user = models.ForeignKey(User)
  link = models.ForeignKey(Link)


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	
	emp_code=models.CharField(max_length=4, unique=True,default='----')
	emp_first_name=models.CharField(max_length=50)
	emp_middle_name=models.CharField(max_length=50)
	emp_last_name=models.CharField(max_length=50)
	emp_address=models.CharField(max_length=300)
	emp_contact_telno=models.IntegerField()
	emp_tin_no=models.IntegerField()
	emp_nationality=models.CharField(max_length=50)
	
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title

#~ class Certificates(models.Model):
	
# Create your models here.
