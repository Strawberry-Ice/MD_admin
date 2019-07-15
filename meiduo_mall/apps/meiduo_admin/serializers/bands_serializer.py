from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from django.conf import settings
from goods.models import Brand


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'logo',
            'first_letter'
        ]