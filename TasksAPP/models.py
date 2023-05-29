import datetime

from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    task_title = models.CharField(max_length=255, blank=False)
    task_description = models.TextField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name_plural = 'Tasks'
