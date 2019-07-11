from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
import pytz

from meiduo_admin.serializers.home_serializer import GoodsDaySerializer
from meiduo_admin.utils import obtain_zero_shanghai
from goods.models import GoodsVisitCount
from orders.models import OrderInfo
from users.models import User


class HomeViewSet(ViewSet):
    # 指定管理员权限才能调用下面接口
    permission_classes = [IsAdminUser]

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

    # 日常活跃用户
    # GET
    # statistical/day_active/
    @action(methods=['get'], detail=False)
    def day_active(self, request):
        # 1.获取当日零时
        date_zero_shanghai = obtain_zero_shanghai()

        # 2.过滤用户
        count = User.objects.filter(last_login__gte=date_zero_shanghai).count()

        # 3.统计数据,构建数据返回
        return Response({
            'count': count,
            'date': date_zero_shanghai
        })

    # 日常下单用户
    # GET
    # statistical/day_orders/
    @action(methods=['get'], detail=False)
    def day_orders(self, request):
        # 1.获取当日零时
        date_zero_shanghai = obtain_zero_shanghai()

        # 2.统计日下单用户

        # 2.1 以从表查询
        # 2.1.1 过滤出当日下单的订单
        # order_queryset = OrderInfo.objects.filter(create_time__gte=date_zero_shanghai)

        # 2.1.2 根据订单,统计出用户
        # user_list = []
        # for order in order_queryset:
        # if order.user not in user_list:
        #     user_list.append(order.user)
        # user_list.append(order.user)

        # 2.1.3 用户去重
        # count = len(user_list)
        # count = len(set(user_list))

        # 2.2 以主表查询
        user_queryset = User.objects.filter(orders__create_time__gte=date_zero_shanghai)
        count = len(set(user_queryset))
        # 3.构建数据返回
        return Response({
            'count': count,
            'date': date_zero_shanghai
        })

    # 获取月增长用户
    # GET
    # tatistical/month_increment/
    @action(methods=['get'], detail=False)
    def month_increment(self, request):
        # 获取最近30天中每一天的用户注册数量
        # 1.构建开始时间点
        # 1.1 当前时间
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE))

        # 1.2 开始时间
        start_date = cur_date - timedelta(days=29)

        # 2.遍历数据
        date_list = []
        for index in range(30):
            # 每遍历一次,获得一个当日时间,然后天数加一
            clac_date = (start_date + timedelta(days=index)).replace(hour=0, minute=0, second=0)

            # 过滤用户
            count = User.objects.filter(date_joined__gte=clac_date,
                                        date_joined__lt=(clac_date + timedelta(days=1))).count()

            # 构建数据
            date_list.append({
                'count': count,
                'date': clac_date.date()
            })

        return Response(date_list)

    # 获取日分类商品访问量
    # GET
    # statistical/goods_day_views/
    @action(methods=['get'], detail=False)
    def goods_day_views(self, request):
        # 1.获取当日零时
        data_zero_shanghai = obtain_zero_shanghai()

        # 2.获得序列化说就
        gv = GoodsVisitCount.objects.filter(create_time__gte=data_zero_shanghai)

        # 3.调用序列化器完成数据序列化
        gvs = GoodsDaySerializer(instance=gv, many=True)

        # 4.响应
        return Response(gvs.data)
