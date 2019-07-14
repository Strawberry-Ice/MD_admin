from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.spec_serializer import SKUSpecSerializer
from goods.models import SPUSpecification
from meiduo_admin.utils import PageNum


class SpecsView(ModelViewSet):
    serializer_class = SKUSpecSerializer
    queryset = SPUSpecification
    pagination_class = PageNum