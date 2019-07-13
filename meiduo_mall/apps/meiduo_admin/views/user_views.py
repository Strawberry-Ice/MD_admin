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