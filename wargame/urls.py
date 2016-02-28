from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import django.views.defaults
from django.views.generic.base import RedirectView, TemplateView
from . import views

CACHE_TIME = 60 * 60

# Site Pages
urlpatterns = [
]
# Views
urlpatterns += [
]
