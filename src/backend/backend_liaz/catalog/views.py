from rest_framework import viewsets

from .models import Unit, Consumable, Part, UnitType
from .serializers import UnitDetailedSerializer, ConsumableDetailedSerializer, PartDetailedSerializer, \
    UnitTypeSerializer, ConsumableSerializer, PartSerializer, UnitSerializer


class UnitTypeViewSet(viewsets.ModelViewSet):
    queryset = UnitType.objects.all().order_by('id')
    serializer_class = UnitTypeSerializer


class ConsumableViewSet(viewsets.ModelViewSet):
    queryset = Consumable.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ConsumableDetailedSerializer
        return ConsumableSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PartDetailedSerializer
        return PartSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UnitDetailedSerializer
        return UnitSerializer
