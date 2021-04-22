from django.contrib import admin

from .models import Chapter, Book


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Chapter)
