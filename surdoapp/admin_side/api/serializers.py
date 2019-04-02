from rest_framework import serializers

from surdoapp.admin_side.models import SurdoWord


class SurdoWordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurdoWord
        fields = ('id', 'name_ru', 'name_kz', 'video_link',)
