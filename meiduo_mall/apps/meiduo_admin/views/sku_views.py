from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.utils import PageNum

from meiduo_admin.serializers.sku_serializer import *
from goods.models import SKU, SPU, SPUSpecification


class SKUGoodsViewSet(ModelViewSet):
    # 指定序列化器
    serializer_class = SKUGoodsSerializer
    # 指定分页器 进行分页返回
    pagination_class = PageNum

    # 重写get_queryset方法，判断是否传递keyword查询参数
    def get_queryset(self):
        # 提取keyword
        keyword = self.request.query_params.get('keyword')

        if keyword == '' or keyword is None:
            return SKU.objects.all()
        else:
            return SKU.objects.filter(name__contains=keyword)


class SKUCategorieView(ListAPIView):
    serializer_class = SKUCategorieSerializer
    # 根据数据存储规律parent_id大于37为三级分类信息，查询条件为parent_id__gt=37
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)


class SPUSimpleView(ListAPIView):
    serializer_class = SPUSimpleSerializer
    queryset = SPU.objects.all()


class SPUSpecView(ListAPIView):
    serializer_class = SPUSpecSerialzier

    # 因为我们继承的是ListAPIView，在拓展类中是通过get_queryset获取数据，但是我们现在要获取的是规格信息，所以重写get_queryset
    def get_queryset(self):
        # 获取spuid值
        pk = self.kwargs['pk']
        # 根据spu的id值关联过滤查询出规格信息

        return SPUSpecification.objects.filter(spu_id=self.kwargs['pk'])
