from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class BlogPost(models.Model):
    content = models.TextField(verbose_name="content of blog")

    def __unicode__(self):
        return self.content


class Comments(models.Model):
    username = models.CharField(verbose_name="Your Name", max_length=20)
    email = models.CharField(verbose_name="Email Addr", max_length=50)
    parent_comment = models.IntegerField(default=0)
    parent_username = models.CharField(max_length=20, default="")
    level = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    blog = models.ForeignKey(BlogPost)

    def __unicode__(self):
        return self.content


admin.site.register(BlogPost)

admin.site.register(Comments)
