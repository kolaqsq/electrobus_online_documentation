from django.contrib import admin
from .models import Part


class PartAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['designation', 'name']


admin.site.register(Part, PartAdmin)
