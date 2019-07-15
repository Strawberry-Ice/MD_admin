from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.bands_serializer import *
from meiduo_admin.utils import PageNum
from goods.models import Brand

class BandViewSet(ModelViewSet):
    serializer_class = BandSerializer
    queryset = Brand.objects.all()
    pagination_class = PageNum