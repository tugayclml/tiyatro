from rest_framework import serializers
from .models import Tiyatro


class TiyatroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiyatro
        fields = ('id', 'title', 'content', 'video_url', 'status', 'created_at', 'updated_at')
