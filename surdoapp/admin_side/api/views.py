from rest_framework import generics

from .serializers import SurdoWordListSerializer
from ..models import SurdoWord


class SurdoWordsByCategory(generics.ListAPIView):
    serializer_class = SurdoWordListSerializer

    def get_queryset(self):
        category = self.kwargs['cat']
        queryset = SurdoWord.objects.filter(category=category)
        return queryset
