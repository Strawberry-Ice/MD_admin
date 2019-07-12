from rest_framework import serializers

from goods.models import SKUSpecification, SKU


class SKUSpecificationSerialzier(serializers.ModelSerializer):
    """
        SKU规格表序列化器
      """

    spec_id = serializers.IntegerField(read_only=True)
    option_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SKUSpecification  # SKUSpecification中sku外键关联了SKU表
        fields = ("spec_id", 'option_id')


class SKUGoodsSerializer(serializers.ModelSerializer):
    """
        获取sku表信息的序列化器
    """
    # 指定所关联的选项信息 关联嵌套返回

    specs = SKUSpecificationSerialzier(read_only=True, many=True)
    # 指定分类信息
    category_id = serializers.IntegerField()
    # 关联嵌套返回
    category = serializers.StringRelatedField(read_only=True)
    # 指定所关联的spu表信息
    spu_id = serializers.IntegerField()
    # 关联嵌套返回
    spu = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'
