from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from apps.blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


# Register your models here.

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
