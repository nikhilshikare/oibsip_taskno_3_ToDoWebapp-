from django.db import models
from zoneinfo import ZoneInfo
from datetime import datetime

# Create your models here.
#<----------Model Todo Table to store all Attendance info Starts Here here ------------>
    # dtobj = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime('%H:%M:%S')
    # strftime('%Y-%m-%d %H:%M:%S.%f')
class TODO(models.Model):
    time = models.DateTimeField(blank=True , null=True)
    completed_time    = models.DateTimeField(blank=True, null=True)
    is_completed  = models.BooleanField(blank=False , default=False)
    username   = models.CharField(max_length=40)
    title  = models.CharField(max_length=150)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.title
