from rest_framework import serializers

from .models import Part, Unit, Consumable, UnitType


class ConsumableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consumable
        fields = ('name', 'desc',)


class PartSerializer(serializers.ModelSerializer):
    consumables = serializers.PrimaryKeyRelatedField(queryset=Consumable.objects.all(), many=True)

    class Meta:
        model = Part
        fields = ('name', 'desc', 'consumables',)


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = ('name',)


class UnitToUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'designation', 'name', 'type',)


class UnitToPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'designation', 'name',)


class UnitToConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = ('id', 'name',)


class UnitSerializer(serializers.ModelSerializer):
    type = UnitTypeSerializer(read_only=True)
    units = UnitToUnitSerializer(read_only=True, many=True)
    parts = UnitToPartSerializer(read_only=True, many=True)
    consumables = UnitToConsumableSerializer(read_only=True, many=True)

    class Meta:
        model = Unit
        fields = ('id', 'designation', 'name', 'type', 'desc', 'units', 'parts', 'consumables',)

# class ConsumableSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Consumable
#         fields = ['name', 'desc']
#
#
# class PartSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Part
#         fields = ['designation', 'name', 'desc', 'consumables']
#
#
# class UnitTypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = UnitType
#         fields = ['name']
#
#
# class UnitSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Unit
#         fields = ['designation', 'name', 'type', 'desc', 'units', 'parts', 'consumables']
