from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.spec_serializer import SKUSpecSerializer
from goods.models import SPUSpecification
from meiduo_admin.utils import PageNum


class SpecsViewSet(ModelViewSet):
    serializer_class = SKUSpecSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = PageNum