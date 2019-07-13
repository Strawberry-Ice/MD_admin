from rest_framework import serializers
from goods.models import SPU


class SPUGoodsSerializer(serializers.ModelSerializer):
    """商品SPU表序列化器"""
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        exclude = ('category1', 'category2', 'category3')
