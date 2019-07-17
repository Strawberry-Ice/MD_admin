from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.permission_serializer import *
from django.contrib.auth.models import Permission
from meiduo_admin.utils import PageNum


class PermissionViewSet(ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    pagination_class = PageNum


class ContentTypeView(ListAPIView):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()