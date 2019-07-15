from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from django.conf import settings
from goods.models import Brand


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'logo',
            'first_letter'
        ]

    # 重写create方法实现FastDFS图片上传
    def create(self, validated_data):

        # 1.创建连接对象
        conn = Fdfs_client(settings.FASTDFS_PATH)

        # 2.获取前端传过来的图片
        file = validated_data.pop('logo')
        content = file.read()

        # 3.上传FastDFS
        res = conn.upload_by_buffer(content)
        if res['Status'] != 'Upload successed.':
            # 上传失败
            raise serializers.ValidationError("上传失败!")

        # 4.修改logo字段
        validated_data['logo'] = res['Remote file_id']

        # 5.响应
        return super().create(validated_data)

    # 重写update方法实现FastDFS图片修改
    def update(self, instance, validated_data):

        # 1.创建连接对象
        conn = Fdfs_client(settings.FASTDFS_PATH)

        # 2.获取前端传过来的图片
        file = validated_data.pop('logo')
        content = file.read()
        # 3.上传DFS
        res = conn.upload_by_buffer(content)
        if res['Status'] != 'Upload successed.':
            # 上传失败
            raise serializers.ValidationError('上传失败!')

        # 4.更新logo字段
        logo = res['Remote file_id']

        instance.logo = logo

        instance=super().update(instance, validated_data)
        # 5.响应
        return instance