from rest_framework import generics

from .serializers import SurdoWordListSerializer
from ..models import SurdoWord


class SurdoWordsByCategory(generics.ListAPIView):
    queryset = SurdoWord.objects.all()
    serializer_class = SurdoWordListSerializer
