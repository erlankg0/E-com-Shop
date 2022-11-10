from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from multiselectfield import MultiSelectField


class Age(models.Model):
    AGE = (
        ("Adult", 'Adult'),
        ("Kids", 'Kids'),
    )
    title = models.CharField(max_length=20, unique=True, verbose_name='Возвраст',
                             help_text='Для взрослых \n Для детей ')
    slug = models.SlugField(unique=True, verbose_name='URL', help_text='Уникальное URL')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраст'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название категории')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, related_name='children', blank=True, null=True,
                            db_index=True, verbose_name='Подкатегория')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название бренда')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Size(models.Model):
    SIZE = (
        ("Oversize", (
            ("S", 'S'),
            ("M", "M"),
            ("L", "L"),
            ("XS", "XS"),
            ("XM", "XM"),
            ("XL", "XL"),
            ("X2L", "X2L"),
            ("X3L", 'X3L'),
        )),
        ("S", 'S'),
        ("M", "M"),
        ("L", "L"),
    )
    size = MultiSelectField(max_length=30, choices=SIZE)

    def __str__(self):
        return self.size


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название продукта')
    description = models.TextField(max_length=5000, verbose_name='Описание продукта')
    size = models.ManyToManyField(Size, related_name='product_size')
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# С мультивыбором
# class Product(models.Model):
#     SIZE = (
#         ("Oversize", (
#             ("S", 'S'),
#             ("M", "M"),
#             ("L", "L"),
#             ("XS", "XS"),
#             ("XM", "XM"),
#             ("XL", "XL"),
#             ("X2L", "X2L"),
#             ("X3L", 'X3L'),
#         )),
#         ("S", 'S'),
#         ("M", "M"),
#         ("L", "L"),
#     )
#     size = MultiSelectField(max_length=30, choices=SIZE)
#     title = models.CharField(max_length=255, unique=True, verbose_name='Название продукта')
#     description = models.TextField(max_length=5000, verbose_name='Описание продукта')
#     price = models.PositiveIntegerField(default=0)
#     discount = models.PositiveIntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
