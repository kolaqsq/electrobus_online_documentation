from django.db import models


class Book(models.Model):
    title = models.CharField('Название книги', max_length=500)
    desc = models.CharField('Описание книги', max_length=1000, blank=True, null=True)
    creation_date = models.DateTimeField('Дата создания')
    is_open = models.BooleanField('Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    title = models.CharField('Название главы', max_length=500)
    content = models.CharField('Текст главы', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
