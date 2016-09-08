from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Project(models.Model):
    project_field = models.CharField(max_length=100)

    def __str__(self):
        return self.project_field


class Post(models.Model):
    employee = models.ForeignKey(User)
    duration_time = models.DecimalField(
            blank=False, null=True,
            max_digits=4, decimal_places=2)
    project_field = models.ForeignKey(Project, blank=True, null=True)
    remarks_field = models.TextField()
    log_date = models.DateTimeField(
            default=timezone.now)
    is_late = models.BooleanField(default=False)

    def __str__(self):
        return '%s at %s' % (self.employee, self.project_field)
