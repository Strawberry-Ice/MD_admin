from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.option_serislizer import OptionSerializer
from goods.models import SpecificationOption
from meiduo_admin.utils import PageNum


class OptionsView(ModelViewSet):
    serializer_class = OptionSerializer
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum