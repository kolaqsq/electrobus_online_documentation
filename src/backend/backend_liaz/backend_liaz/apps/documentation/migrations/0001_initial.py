# Generated by Django 3.2 on 2021-04-22 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название книги')),
                ('desc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание книги')),
                ('creation_date', models.DateTimeField(verbose_name='Дата создания')),
                ('is_open', models.BooleanField(verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название главы')),
                ('content', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Текст главы')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentation.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
            },
        ),
    ]
