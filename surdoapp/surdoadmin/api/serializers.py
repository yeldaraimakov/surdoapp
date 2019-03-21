from rest_framework import serializers

from surdoapp.surdoadmin.models import SurdoWord

class SurdoWordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurdoWord
        fields = ('id', 'name', 'video_link',)
