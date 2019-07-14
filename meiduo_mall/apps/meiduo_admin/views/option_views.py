from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.option_serislizer import OptionSerializer
from meiduo_admin.serializers.spec_serializer import SKUSpecSerializer
from goods.models import SpecificationOption, SPUSpecification
from meiduo_admin.utils import PageNum


class OptionsView(ModelViewSet):
    serializer_class = OptionSerializer
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum


class OptionSimpleView(ListAPIView):
    serializer_class = SKUSpecSerializer
    queryset = SPUSpecification.objects.all()
