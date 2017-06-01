from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return '[Teacher] {}'.format(self.user.username)


class Class(models.Model):
    class_name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, related_name='classes')

    def __str__(self):
        return '[Class] {}'.format(self.class_name)


class Student(models.Model):
    user = models.OneToOneField(User)
    joined_class = models.ForeignKey(Class, related_name='students')

    def __str__(self):
        return '[Student] {}'.format(self.user.username)


class Parent(models.Model):
    user = models.OneToOneField(User)
    children = models.ManyToManyField(Student, related_name='parents')

    def __str__(self):
        return '[Parent] {}'.format(self.user.username)


class Post(models.Model):
    posted_by = models.ForeignKey(Teacher, related_name='posted')
    related_to = models.ForeignKey(Student, related_name='related_posts')
    image = models.ImageField(upload_to='uploads/')
    upload_datetime = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
