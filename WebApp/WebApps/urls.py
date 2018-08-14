"""Defines URL patterns for WebApps"""

from django.conf.urls import url
from . import views

app_name = 'WebApps'
urlpatterns = [
    # Home Page
    url('', views.index, name='index')

]
