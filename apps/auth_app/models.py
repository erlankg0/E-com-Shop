from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.auth_app.country_list import get_countries, get_country_and_province


# class Address(models.Model):
#     address = models.TextField(
#         max_length=500,
#         unique=True,
#         verbose_name='Адрес'
#     )
#
#     def __str__(self):
#         return self.address


class Choices(models.Model):
    country = models.CharField(max_length=555, choices=get_country_and_province())

    def __str__(self):
        return self.country

# class ShopUser(AbstractUser):
#     COUNTRY_WITH_PROVINCE = (
#         ("Kyrgyzstan",
#          ("CHUY1", "CHUY1"),
#          ("CHUY2", "CHUY2"),
#          ("CHUY3", "CHUY3"),
#          ("CHUY4", "CHUY4"),
#          ("CHUY5", "CHUY5"),
#          ),
#         ("Kazakstan",
#          ("AlMA1", "AlMA1"),
#          ("AlMA2", "AlMA2"),
#          ("AlMA3", "AlMA3"),
#          ("AlMA4", "AlMA4"),
#          ("AlMA5", "AlMA5"),
#          ),
#     )
#     country = models.CharField(
#         verbose_name='Страна',
#         max_length=150,
#         choices=COUNTRY_WITH_PROVINCE,
#     )
#     province = models.CharField()
#     town = models.CharField()
#     phone_number = models.CharField()
#     address = models.ManyToManyField(
#         Address,
#         verbose_name='Адреса'
#     )
