from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Collection(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название коллекции'
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = "Коллекции"
        ordering = ['-title']


class Category(MPTTModel):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT,
        verbose_name='Привязка категории к коллекции'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        db_index=True,
        verbose_name='Категория к в коллекции'
    )
