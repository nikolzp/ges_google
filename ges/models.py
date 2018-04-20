from django.db import models


class Ges(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    coordinates_lat = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='lat')
    coordinates_lan = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='lan')
    country = models.CharField(max_length=30, verbose_name='Страна')
    river = models.CharField(max_length=30, verbose_name='Река')
    power = models.IntegerField(verbose_name='Мощность')
    annual_average = models.FloatField(blank=True, null=True, verbose_name='Среднегодовая выработка')
    area_reservoir = models.IntegerField(blank=True, null=True, verbose_name='Площадь водохранилища')

    def __str__(self):
        return self.name