from django.db import models


class MythicDifficult(models.Model):
    name = models.CharField(max_length=255, verbose_name='Уровень сложности')
    description = models.TextField(verbose_name='Описание')
    priceInDollars = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена в долларах')
    priceInEuro = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена в евро')

    def __str__(self):
        return self.name


class MythicOption(models.Model):
    name = models.CharField(max_length=255, verbose_name='Опция')
    priceInDollars = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена в долларах')
    priceInEuro = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена в евро')

    def __str__(self):
        return self.name
