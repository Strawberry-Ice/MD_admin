from rest_framework import serializers
from goods.models import SPU, Brand, GoodsCategory


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


class SPUBrandSerializer(serializers.ModelSerializer):
    """SPU表品牌序列化器"""

    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """SPU表分类信息获取序列化器"""

    class Meta:
        model = GoodsCategory
        fields = "__all__"
