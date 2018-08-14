# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for WebApps"""
    return render(request, 'WebApps/index.html')
