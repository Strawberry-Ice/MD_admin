from rest_framework.generics import ListAPIView
from meiduo_admin.serializers.user_manage_serializer import UserSerializer
from meiduo_admin.utils import UserPageNum
from users.models import User


class UserView(ListAPIView):
    # 指定序列化器
    serializer_class = UserSerializer

    # 指定分液器
    pagination_class = UserPageNum

    # 重写get_queryset方法,根据前端是否传递keyword值返回不同的查询结果
    def get_queryset(self):

        # 获取keyword
        keyword = self.request.query_params.get('keyword')

        # keyword为空,说明要获取所有数据
        if keyword is '' or keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username=keyword)

