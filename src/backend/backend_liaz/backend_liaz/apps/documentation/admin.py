from django.contrib import admin
import nested_admin

from .models import Chapter, Book, Subsection, Section


class SubsectionInline(nested_admin.NestedStackedInline):
    model = Subsection
    extra = 0
    show_change_link = True


class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    extra = 0
    show_change_link = True
    inlines = [SubsectionInline]


class ChapterInline(nested_admin.NestedStackedInline):
    model = Chapter
    extra = 0
    show_change_link = True
    inlines = [SectionInline]


class SectionAdmin(nested_admin.NestedModelAdmin):
    inlines = [SubsectionInline]


class ChapterAdmin(nested_admin.NestedModelAdmin):
    inlines = [SectionInline]


class BookAdmin(nested_admin.NestedModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection)
