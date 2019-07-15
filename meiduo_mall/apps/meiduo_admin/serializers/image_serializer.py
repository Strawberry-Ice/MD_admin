from fdfs_client.client import Fdfs_client
from rest_framework import serializers
from django.conf import settings

from goods.models import SKUImage, SKU


class ImageSerializer(serializers.ModelSerializer):
    # sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = '__all__'

    def create(self, validated_data):

        # 1.创建FastDFS连接对象
        conn = Fdfs_client(settings.FASTDFS_PATH)

        # 2.获取前端传递的image文件
        file = validated_data.pop('image')
        content = file.read() # content: 上传来的文件"数据" byte:字节对象

        # 3.根据文件上传FastDFS
        res = conn.upload_by_buffer(content)
        if res['Status'] != 'Upload successed.':
            # 上传失败
            raise serializers.ValidationError("上传失败!")

        validated_data['image'] = res['Remote file_id']

        # sku_id = validated_data['sku'].id
        # image_url = validated_data['image']
        # 更新商品默认显示的图片
        SKU.objects.filter(id=validated_data['sku'].id).update(default_image=validated_data['image'])
        # 4.返回响应
        return super().create(validated_data)

    def update(self, instance, validated_data):
        file = validated_data.pop("image")
        content = file.read()  # content: 上传来的文件"数据" byte:字节对象

        # 1.2 获得fdfs链接对象
        # conn = Fdfs_client('./meiduo_mall/client.conf')
        conn = Fdfs_client(settings.FDFS_CONFPATH)
        # 1.3 根据文件数据上传
        res = conn.upload_by_buffer(content)  # 传入数据也是字节对象
        if res['Status'] != 'Upload successed.':
            # 上传失败
            raise serializers.ValidationError("上传失败！")

        instance.image = res['Remote file_id']
        instance.save()

        return instance


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields=['id', 'name']