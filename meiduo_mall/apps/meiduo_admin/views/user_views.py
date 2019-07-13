from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.utils import PageNum

from meiduo_admin.serializers.sku_serializer import *
from meiduo_admin.serializers.user_serializer import *
from users.models import User
from goods.models import SKU, SPU, SPUSpecification


class UserView(ListCreateAPIView):
    # 指定使用的序列化器
    serializer_class = UserSerializer
    # 指定分页器
    pagination_class = PageNum

    def get_serializer_class(self):
        # 请求方式是GET，则是获取用户数据返回UserSerializer
        if self.request.method == 'GET':
            return UserSerializer
        else:
            # POST请求，完成保存用户，返回UserAddSerializer
            return UserAddSerializer

    # 重写get_queryset方法，根据前端是否传递keyword值返回不同查询结果
    def get_queryset(self):
        # 获取前端传递的keyword值
        keyword = self.request.query_params.get('keyword')
        # 如果keyword是空字符，则说明要获取所有用户数据
        if keyword is '' or keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=keyword)


class SKUGoodsView(ModelViewSet):
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
