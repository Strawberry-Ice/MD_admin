from rest_framework import serializers

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory


class ChannelsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    group = serializers.StringRelatedField()
    group_id = serializers.IntegerField()

    class Meta:
        model = GoodsChannel
        fields = [
            'id',
            'category',
            'category_id',
            'group',
            'group_id',
            'sequence',
            'url'
        ]


class ChannelsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsChannelGroup
        fields = [
            'id',
            'name'
        ]


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = [
            'id',
            'name'
        ]