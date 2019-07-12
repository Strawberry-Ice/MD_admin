from rest_framework.generics import ListAPIView, ListCreateAPIView
from meiduo_admin.serializers.user_manage_serializer import UserSerializer, UserAddSerializer
from meiduo_admin.utils import UserPageNum
from users.models import User


class UserView(ListCreateAPIView):
    # 指定序列化器
    serializer_class = UserSerializer

    # 指定分液器
    pagination_class = UserPageNum

    # 根据不同的请求方式返回不同序列化器
    def get_serializer_class(self):
        # 请求方式是GET，则是获取用户数据返回UserSerializer
        if self.request.method == 'GET':
            return UserSerializer
        if self.request.method == 'POST':
            # POST请求，完成保存用户，返回UserAddSerializer
            return UserAddSerializer

    # 重写get_queryset方法,根据前端是否传递keyword值返回不同的查询结果
    def get_queryset(self):

        # 获取keyword
        keyword = self.request.query_params.get('keyword')

        # keyword为空,说明要获取所有数据
        if keyword is '' or keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=keyword)
