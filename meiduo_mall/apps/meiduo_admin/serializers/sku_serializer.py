from rest_framework import serializers

from goods.models import SKUSpecification, SKU, GoodsCategory, SpecificationOption, SPUSpecification


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


class SKUCategorieSerializer(serializers.ModelSerializer):
    """
        商品分类序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class SPUSimpleSerializer(serializers.ModelSerializer):
    """
        商品SPU表序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')


class SPUOptineSerializer(serializers.ModelSerializer):
    """
        规格选项序列化器
    """

    class Meta:
        model = SpecificationOption
        fields = ('id', 'value')


class SPUSpecSerialzier(serializers.ModelSerializer):
    """
        规格序列化器
    """
    # 关联序列化返回SPU表数据
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField(read_only=True)
    # 关联序列化返回 规格选项信息
    options = SPUOptineSerializer(read_only=True, many=True)  # 使用规格选项序列化器

    class Meta:
        model = SPUSpecification  # SPUSpecification中的外键spu关联了SPU商品表
        fields = "__all__"
