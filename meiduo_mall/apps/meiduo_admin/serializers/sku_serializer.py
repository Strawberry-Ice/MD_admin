from rest_framework import serializers

from goods.models import SKU, SKUSpecification


class SKUSpecSerializer(serializers.ModelSerializer):

    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ['spec_id', 'option_id']


class SKUSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    # 嵌套序列化
    spec = SKUSpecSerializer(many=True, read_only=True)

    class Meta:
        model = SKU
        fields = '__all__'
