from django.contrib.postgres.fields import ArrayField
from django.db import models

#
# class Order(models.Model):
#
#     name = models.CharField(max_length=255, verbose_name='Наименование активности')
#     difficult = models.CharField(max_length=100, verbose_name='Сложность')
#     priceInDollars = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена в долларах')
#     priceInEuro = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена в евро')
#     options = ArrayField(
#         ArrayField(
#             models.CharField(max_length=100, blank=True),
#             size=10,
#         ),
#         size=10,
#     )
#
#     def __str__(self):
#         return self.name
