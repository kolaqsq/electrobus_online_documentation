from django.contrib import admin

from .models import Part, Unit


class UnitAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['designation', 'name']

    filter_horizontal = ('parts', 'consumables')


class PartAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['designation', 'name']


admin.site.register(Part, PartAdmin)
admin.site.register(Unit, UnitAdmin)
