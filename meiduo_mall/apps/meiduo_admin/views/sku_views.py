from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.sku_serializer import SKUSerializer
from meiduo_admin.utils import PageNum
from goods.models import SKU

# GET
# meiduo_admin/skus/?page=1&pagesize=10&keyword=
class SKUGoodsView(ModelViewSet):# (ListAPIView):
    # 指定序列化器
    serializer_class = SKUSerializer
    # 指定分页器
    pagination_class = PageNum

    # 重写get_queryset方法，判断是否传递keyword查询参数
    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')

        if keyword:
            return SKU.objects.filter(name__contains=keyword)
        else:
            return SKU.objects.all()
