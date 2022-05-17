from django.contrib import admin

from . import models

admin.site.register(models.Item)
admin.site.register(models.Photo)
admin.site.register(models.Title)
admin.site.register(models.Client)
