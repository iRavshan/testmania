from django.contrib import admin
from . import models

admin.site.register(models.Test)
admin.site.register(models.TestScore)
admin.site.register(models.Subject)