from django.db import models
from django.utils.translation import ugettext_lazy


class Drink(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название напитка")
    drink_title = models.CharField(max_length=100, verbose_name="Тип напитка")
    description= models.CharField(max_length=100, verbose_name="Описание")

    #Возвращение дефолтное значение при оброщении к обьекту
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ugettext_lazy("напиток")
        verbose_name_plural = ugettext_lazy("напитки")

class Logins(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=" имя")
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')


    def __str__(self):
        return self.first_name + "   " + self.last_name