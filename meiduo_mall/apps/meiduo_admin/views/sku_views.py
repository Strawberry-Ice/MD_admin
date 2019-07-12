from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from meiduo_admin.serializers.sku_serializer import *
from meiduo_admin.utils import PageNum
from goods.models import SKU


# GET
# /skus/?page=1&pagesize=10&keyword=
class SKUGoodsView(ModelViewSet):  # (ListAPIView):
    # 指定序列化器
    serializer_class = SKUSerializer
    # 指定分页器
    pagination_class = PageNum

    queryset = SKU.objects.all()

    # 重写get_queryset方法，判断是否传递keyword查询参数
    def get_queryset(self):
        if self.action == "categories":
            return GoodsCategory.objects.filter(parent_id__gt=37)
        if self.action == "simple":
            return SPU.objects.all()

        keyword = self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        else:
            return self.queryset.all()

    def get_serializer_class(self):
        if self.action == "categories":
            return GoodsCategorieSerializer
        if self.action == "simple":
            return SPUSimpleSerializer

        return self.serializer_class

    # GET
    # /skus/categories/
    @action(methods=['get'], detail=False)
    def categories(self, request):
        """返回三级数据"""
        cates = self.get_queryset()

        cates_serializer = self.get_serializer(cates, many=True)
        return Response(cates_serializer.data)

    # GET
    # /goods/simple/
    @action(methods=['get'], detail=False)
    def simple(self, request):
        spu_query = self.get_queryset()
        spu_serializer = self.get_serializer(spu_query, many=True)
        return Response(spu_serializer.data)