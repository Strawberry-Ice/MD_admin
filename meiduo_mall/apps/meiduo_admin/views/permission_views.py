from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.permission_serializer import PermissionSerializer
from django.contrib.auth.models import Permission
from meiduo_admin.utils import PageNum


class PermissionViewSet(ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    pagination_class = PageNum
