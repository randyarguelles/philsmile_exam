from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

	


class Post(models.Model):
	employee =models.CharField(max_length=200)
	duration_time= models.DecimalField(
			blank=False, null=True,
			max_digits=4, decimal_places=2)
	project_field=models.CharField(max_length=100)
	remarks_field = models.TextField()
	log_date = models.DateTimeField(
			default=timezone.now)

	
	

#~ class Certificates(models.Model):
	
# Create your models here.
