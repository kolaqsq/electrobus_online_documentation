from rest_framework import serializers

from .models import Part, Unit, Consumable, UnitType


class UnitTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitType
        fields = ('name',)


class ConsumableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consumable
        fields = ('url', 'name',)


class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ('url', 'designation', 'name',)


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    type = UnitTypeSerializer(read_only=True)

    class Meta:
        model = Unit
        fields = ('url', 'designation', 'name', 'type',)


class ConsumableDetailedSerializer(serializers.HyperlinkedModelSerializer):
    parts_cons = PartSerializer(read_only=True, many=True)
    units_cons = UnitSerializer(read_only=True, many=True)

    class Meta:
        model = Consumable
        fields = ('id', 'url', 'name', 'desc', 'parts_cons', 'units_cons',)


class PartDetailedSerializer(serializers.HyperlinkedModelSerializer):
    consumables = ConsumableSerializer(read_only=True, many=True)
    units_parts = UnitSerializer(read_only=True, many=True)

    class Meta:
        model = Part
        fields = ('id', 'url', 'designation', 'name', 'desc', 'consumables', 'units_parts',)


class UnitDetailedSerializer(serializers.HyperlinkedModelSerializer):
    type = UnitTypeSerializer(read_only=True)
    units = UnitSerializer(read_only=True, many=True)
    parts = PartSerializer(read_only=True, many=True)
    consumables = ConsumableSerializer(read_only=True, many=True)

    class Meta:
        model = Unit
        fields = ('id', 'url', 'designation', 'name', 'type', 'desc', 'units', 'parts', 'consumables',)
