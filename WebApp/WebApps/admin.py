# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from WebApps.models import Course
from WebApps.models import Entry

# Register your models here.
admin.site.register(Course)
admin.site.register(Entry)

