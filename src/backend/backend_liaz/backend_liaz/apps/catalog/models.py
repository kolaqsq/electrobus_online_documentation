from django.db import models
from ckeditor.fields import RichTextField


class Part(models.Model):
    designation = models.CharField('Обозначение', max_length=100)
    name = models.CharField('Наименование', max_length=500)
    desc = RichTextField('Описание', max_length=1000, blank=True, null=True)

    def __str__(self):
        template = '{0.designation} {0.name}'
        return template.format(self)

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'
