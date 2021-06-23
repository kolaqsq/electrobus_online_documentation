from rest_framework import viewsets

from .models import Unit, Consumable, Part, UnitType
from .serializers import UnitSerializer, ConsumableSerializer, PartSerializer, UnitTypeSerializer


class ConsumableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consumable.objects.all().order_by('id')
    serializer_class = ConsumableSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Part.objects.all().order_by('id')
    serializer_class = PartSerializer


class UnitTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UnitType.objects.all().order_by('id')
    serializer_class = UnitTypeSerializer


class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Unit.objects.all().order_by('id')
    serializer_class = UnitSerializer
