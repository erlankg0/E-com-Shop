from django.contrib import admin
from apps.products import models
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(models.Age)
class AgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title", 'parent',)}


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Quantity)
class QuantityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', 'size', 'category',)}

# Register your models here.
# admin.site.register(models.Size)
# admin.site.register(models.Brand)
# admin.site.register(models.Category)
# admin.site.register(models.Age)
# admin.site.register(models.Product)
# admin.site.register(models.Quantity)
