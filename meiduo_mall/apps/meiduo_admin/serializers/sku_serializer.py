from rest_framework import serializers

from goods.models import SKUSpecification, SKU, GoodsCategory, SpecificationOption, SPUSpecification


class SKUSpecificationSerialzier(serializers.ModelSerializer):
    """
        SKU规格表序列化器
      """

    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification  # SKUSpecification中sku外键关联了SKU表
        fields = ("spec_id", 'option_id')


class SKUGoodsSerializer(serializers.ModelSerializer):
    """获取sku表信息的序列化器"""
    # 指定所关联的选项信息 关联嵌套返回

    # 指定分类信息
    category_id = serializers.IntegerField()
    # 关联嵌套返回
    category = serializers.StringRelatedField(read_only=True)
    # 指定所关联的spu表信息
    spu_id = serializers.IntegerField()
    # 关联嵌套返回
    spu = serializers.StringRelatedField(read_only=True)
    # specs 指的是什么? 与当前sku对象关联所有从表（SKUSpecification）数据集
    specs = SKUSpecificationSerialzier(many=True)

    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'

    def create(self, validated_data):
        # 新建单一sku对象的时候, 手动构建中间表数据, 来保存规格和选项信息
        # [
        #      {"spec_id": 4, "option_id": 9},
        #      ...
        # ]
        specs = validated_data.pop('specs')

        # 创建从表数据对象之前, 先创建主表sku对象
        instance = super().create(validated_data)

        # 遍历出有几个规格
        for temp in specs:
            temp['sku_id'] = instance.id
            SKUSpecification.objects.create(**temp)
        return instance

    def update(self, instance, validated_data):
        specs = validated_data.pop('spesc')
        # 原来的中间表数据
        # [
        #      {"spec_id": 4, "option_id": 9},
        #      {}
        # ]

        # [
        # {"spec_id": 4, "option_id": 8},
        # {},
        # ....
        # ]

        # 更新中间表
        # for temp in specs:
        #     # temp: {"spec_id": 4, "option_id": 8}
        #     # 获取中间表对象
        #     sku_spec = SKUSpecification.objects.get(sku_id=instance.id, spec_id=temp['spec_id'])
        #     sku_spec.option_id = temp['option_id']
        #     sku_spec.save()

        # 如果该sku对象，关联的spu更改了，规格变
        # 1、先删除中间表数据
        SKUSpecification.objects.filter(sku_id=instance.id).delete()
        # 2、根据新的规格选项区新建
        for temp in specs:
            # {"sku_id": instance.id, "spec_id": 4, "option_id": 8}
            temp['sku_id'] = instance.id
            SKUSpecification.objects.create(**temp)

        # 实现sku对象更新
        return super().update(instance, validated_data)


class SKUCategorieSerializer(serializers.ModelSerializer):
    """商品分类序列化器"""

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class SPUSimpleSerializer(serializers.ModelSerializer):
    """商品SPU表序列化器"""

    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')


class SPUOptineSerializer(serializers.ModelSerializer):
    """规格选项序列化器"""

    class Meta:
        model = SpecificationOption
        fields = ('id', 'value')


class SPUSpecSerialzier(serializers.ModelSerializer):
    """规格序列化器"""
    # 关联序列化返回SPU表数据
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField(read_only=True)
    # 关联序列化返回 规格选项信息
    options = SPUOptineSerializer(read_only=True, many=True)  # 使用规格选项序列化器

    class Meta:
        model = SPUSpecification  # SPUSpecification中的外键spu关联了SPU商品表
        fields = "__all__"
