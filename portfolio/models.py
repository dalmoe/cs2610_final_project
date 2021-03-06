from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=32)
    project_description = models.TextField(default="")
    project_source = models.URLField(default="")
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.project_name;
    