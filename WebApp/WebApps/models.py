# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Course(models.Model):
    """A course that the user is taking"""
    course = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a String representation of a course"""
        return self.course


class Entry(models.Model):
    """Something mentioned about a course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a string representation of the model"""
        return self.text[:50] + "..."
