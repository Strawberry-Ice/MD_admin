from rest_framework import serializers

from goods.models import SPUSpecification


class SKUSpecSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = '__all__'
