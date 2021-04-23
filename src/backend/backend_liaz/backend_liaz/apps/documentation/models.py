from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Book(models.Model):
    title = models.CharField('Название книги', max_length=500)
    desc = RichTextUploadingField('Описание книги', max_length=1000, blank=True, null=True)
    published = models.BooleanField('Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    title = models.CharField('Название главы', max_length=500)
    content = RichTextUploadingField('Текст главы', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'


class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Глава')
    title = models.CharField('Название секции', max_length=500)
    content = RichTextUploadingField('Текст секции', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Секция')
    title = models.CharField('Название подсекции', max_length=500)
    content = RichTextUploadingField('Текст подсекции', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подсекция'
        verbose_name_plural = 'Подсекции'
