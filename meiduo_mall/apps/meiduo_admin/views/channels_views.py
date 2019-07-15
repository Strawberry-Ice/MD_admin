from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.channels_serializer import *
from meiduo_admin.utils import PageNum
from goods.models import GoodsChannel


class ChannelsViewSet(ModelViewSet):
    serializer_class = ChannelsSerializer
    queryset = GoodsChannel.objects.all()
    pagination_class = PageNum