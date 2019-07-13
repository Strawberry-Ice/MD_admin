from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from meiduo_admin.serializers.spu_serializer import SPUGoodsSerializer
from meiduo_admin.utils import PageNum
from goods.models import SPU


class SPUGoodsView(ModelViewSet):
    # 指定序列化器
    serializer_class = SPUGoodsSerializer
    # 指定分页器
    pagination_class = PageNum
    # 指定查询集
    queryset = SPU.objects.all()