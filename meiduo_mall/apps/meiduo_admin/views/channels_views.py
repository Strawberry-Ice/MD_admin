from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.channels_serializer import *
from meiduo_admin.utils import PageNum
from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory


class ChannelsViewSet(ModelViewSet):
    serializer_class = ChannelsSerializer
    queryset = GoodsChannel.objects.all()
    pagination_class = PageNum


class ChannelsSimplView(ListAPIView):
    serializer_class = ChannelsSimpleSerializer
    queryset = GoodsChannelGroup.objects.all()


class GoodsCategoryView(ListAPIView):
    serializer_class = GoodsCategorySerializer
    queryset = GoodsCategory.objects.all()