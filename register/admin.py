from django.contrib import admin
from django.db import OperationalError
# Register your models here.
from .models import Profile
admin.site.register(Profile)
