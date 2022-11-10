from django.contrib import admin
from apps.products import models

# Register your models here.
admin.site.register(models.Size)
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Age)

