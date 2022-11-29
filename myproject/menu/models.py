from django.db import models


class Subdivision(models.Model):
    """ Subdivision model """
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100, verbose_name='Слаг')
    order = models.IntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name='Подразделение')

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ("order",)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    """ Employee model """
    full_name = models.CharField(max_length=250, verbose_name='Полное имя')
    position = models.CharField(max_length=250, verbose_name='Позиция')
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    hiring = models.DateField(verbose_name='Дата')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE,
                                    verbose_name='Подразделение')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f'{self.full_name}'
