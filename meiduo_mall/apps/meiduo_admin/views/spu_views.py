from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from meiduo_admin.serializers.spu_serializer import *
from meiduo_admin.utils import PageNum
from goods.models import SPU, Brand, GoodsCategory


class SPUGoodsViewSet(ModelViewSet):
    # 指定序列化器
    serializer_class = SPUGoodsSerializer
    # 指定分页器
    pagination_class = PageNum
    # 指定查询集
    queryset = SPU.objects.all()

    def get_queryset(self):
        if self.action == "simple":
            return Brand.objects.all()

        if self.action == "categories":
            return GoodsCategory.objects.all()

        if self.action == "channel":
            return GoodsCategory.objects.filter(parent=self.kwargs['pk'])

        return SPU.objects.all()

    def get_serializer_class(self):
        if self.action == "simple":
            return SPUBrandSerializer

        if self.action == "categories":
            return CategorySerializer

        if self.action == "channel":
            return CategorySerializer

        return SPUGoodsSerializer
    # GET
    # /goods/brands/simple
    @action(methods=['get'], detail=False)
    def simple(self, request):
        brand_query = self.get_queryset()
        brand_serializer = self.get_serializer(brand_query, many=True)
        return Response(brand_serializer.data)

    # GET
    # goods/channel/categories/
    @action(methods=['get'], detail=False)
    def categories(self, request):
        cate_query = self.get_queryset()
        cate_serializer = self.get_serializer(cate_query, many=True)
        return Response(cate_serializer.data)

    # GET
    # goods/channel/categories/(?P<pk>\d+)/
    @action(methods=['get'], detail=True)
    def channel(self, request, pk):
        chan_query = self.get_queryset()
        chan_serializer = self.get_serializer(chan_query, many=True)
        return Response(chan_serializer.data)













