from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.order_serializer import *
from meiduo_admin.utils import PageNum
from orders.models import OrderInfo


class OrdersView(ModelViewSet):
    serializer_class = OrderSeriazlier
    queryset = OrderInfo.objects.all()
    pagination_class = PageNum