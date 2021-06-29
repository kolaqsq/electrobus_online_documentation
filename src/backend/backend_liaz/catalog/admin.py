from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _

from .models import Part, Unit, Consumable, UnitType


class UnitAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['type', 'designation', 'name']

    search_fields = ['type', 'designation', 'name']
    list_filter = ['type', ]

    filter_horizontal = ('units', 'parts', 'consumables',)


class PartAdminForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'

    units_parts = forms.ModelMultipleChoiceField(
        label='Связанные узлы',
        queryset=Unit.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Узлы'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(PartAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['units_parts'].initial = self.instance.units_parts.all()

    def save(self, commit=True):
        part = super(PartAdminForm, self).save(commit=False)
        part.save()
        part.units_parts.set(self.cleaned_data['units_parts'])
        return part


class PartAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['designation', 'name']

    search_fields = ['designation', 'name']

    form = PartAdminForm
    filter_horizontal = ('consumables',)


class ConsumableAdminForm(forms.ModelForm):
    class Meta:
        model = Consumable
        fields = '__all__'

    units_cons = forms.ModelMultipleChoiceField(
        label='Связанные узлы',
        queryset=Unit.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Узлы'),
            is_stacked=False
        )
    )

    parts_cons = forms.ModelMultipleChoiceField(
        label='Связанные детали',
        queryset=Part.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Детали'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(ConsumableAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['units_cons'].initial = self.instance.units_cons.all()

        if self.instance and self.instance.pk:
            self.fields['parts_cons'].initial = self.instance.parts_cons.all()

    def save(self, commit=True):
        cons = super(ConsumableAdminForm, self).save(commit=False)
        cons.save()
        cons.units_cons.set(self.cleaned_data['units_cons'])
        cons.parts_cons.set(self.cleaned_data['parts_cons'])
        return cons


class ConsumableAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['name']

    search_fields = ['name']

    form = ConsumableAdminForm


class UnitTypeAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return ['name']

    search_fields = ['name']


admin.site.register(Unit, UnitAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Consumable, ConsumableAdmin)
admin.site.register(UnitType, UnitTypeAdmin)
