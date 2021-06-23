from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Consumable(models.Model):
    name = models.CharField('Наименование', max_length=500)
    desc = RichTextUploadingField('Описание', max_length=1000, blank=True, null=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name = 'Расходный материал'
        verbose_name_plural = 'Расходные материалы'


class Part(models.Model):
    designation = models.CharField('Обозначение', max_length=100)
    name = models.CharField('Наименование', max_length=500)
    desc = RichTextUploadingField('Описание', max_length=1000, blank=True, null=True)
    consumables = models.ManyToManyField(Consumable, verbose_name='Связанные расходные материалы',
                                         related_name='parts_cons', symmetrical=True, blank=True)

    def __str__(self):
        template = '{0.designation} {0.name}'
        return template.format(self)

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class UnitType(models.Model):
    name = models.CharField('Нименование', max_length=100)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name = 'Тип узла'
        verbose_name_plural = 'Типы узлов'


class Unit(models.Model):
    designation = models.CharField('Обозначение', max_length=100)
    name = models.CharField('Наименование', max_length=500)
    type = models.ForeignKey(UnitType, verbose_name='Тип узла', on_delete=models.PROTECT)
    desc = RichTextUploadingField('Описание', max_length=1000, blank=True, null=True)
    units = models.ManyToManyField('self', verbose_name='Связанные узлы', blank=True)
    parts = models.ManyToManyField(Part, verbose_name='Связанные запчасти', related_name='units_parts',
                                   symmetrical=True, blank=True)
    consumables = models.ManyToManyField(Consumable, verbose_name='Связанные расходники', related_name='units_cons',
                                         symmetrical=True, blank=True)

    def __str__(self):
        template = '{0.designation} {0.name}'
        return template.format(self)

    class Meta:
        verbose_name = 'Узел'
        verbose_name_plural = 'Узлы'

