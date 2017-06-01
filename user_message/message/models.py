from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class Message(models.Model):
    from_user = models.IntegerField(verbose_name="from")
    to_user = models.IntegerField(verbose_name="to")
    contents = models.CharField(verbose_name="contents of message", default="",
                                max_length=200)
    create_time = models.DateTimeField()


admin.site.register(Message)
