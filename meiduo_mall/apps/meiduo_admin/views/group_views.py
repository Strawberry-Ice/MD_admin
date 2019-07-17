from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import Group, Permission

from meiduo_admin.serializers.group_serializer import GroupSerializer
from meiduo_admin.serializers.permission_serializer import PermissionSerializer
from meiduo_admin.utils import PageNum


class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    pagination_class = PageNum


class GroupSimpleView(ListAPIView):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()