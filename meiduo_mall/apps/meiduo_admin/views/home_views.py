from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import User
from django.utils import timezone

from meiduo_admin.utils import obtain_zero_shanghai


class HomeViewSet(ViewSet):

    # 获取用户总数
    # GET
    # statistical/total_count/
    @action(methods=['get'], detail=False)
    def total_count(self, request):
        count = User.objects.count()

        date = timezone.now().date()

        return Response({
            'count': count,
            'date': date
        })

    # 用户日增人数
    # GET
    # statistical/day_increment/
    @action(methods=['get'], detail=False)
    def day_increment(self, request):
        # 1.获取当日零时
        date_zero_shanghai = obtain_zero_shanghai()

        # 2.根据零时过滤用户
        count = User.objects.filter(date_joined__gte=date_zero_shanghai).count()

        # 3.构建响应数据
        return Response({
            'count': count,
            'date': date_zero_shanghai
        })
