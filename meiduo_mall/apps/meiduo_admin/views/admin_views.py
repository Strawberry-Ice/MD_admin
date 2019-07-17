from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.admin_serializer import AdminSerializer
from meiduo_admin.serializers.group_serializer import GroupSerializer
from django.contrib.auth.models import Group
from meiduo_admin.utils import PageNum
from users.models import User


class AdminViewSet(ModelViewSet):
    serializer_class = AdminSerializer
    queryset = User.objects.filter(is_staff=True)
    pagination_class = PageNum


class AdminSimpleView(ListAPIView):
    serializer_class =GroupSerializer
    queryset = Group.objects.all()
