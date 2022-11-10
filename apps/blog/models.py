from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post title')
    slug = models.SlugField(max_length=150, unique=True)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Category')
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Category title')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, db_index=True,
                            verbose_name='Parent category', related_name='children')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('post-by-category', kwargs={"slug": self.slug})
