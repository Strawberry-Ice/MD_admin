from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from fdfs_client.client import Fdfs_client
from django.conf import settings

from meiduo_admin.serializers.image_serializer import *
from meiduo_admin.utils import PageNum
from goods.models import SKUImage, SKU


class ImageView(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = SKUImage.objects.all()
    pagination_class = PageNum

    # GET
    # /meiduo_admin/skus/simple/
    def simple(self, request):
        query = SKU.objects.all()
        ser = SKUSerializer(query, many=True)

        return Response(ser.data)

    # 重写拓展类的保存业务逻辑
    def create(self, request, *args, **kwargs):
        # 创建FastDFS连接对象
        client = Fdfs_client(settings.FASTDFS_PATH)
        # 获取前端传递的image文件
        data = request.FILES.get('image')
        # 上传图片到fastDFS
        res = client.upload_by_buffer(data.read())
        # 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            return Response(status=403)
        # 获取上传后的路径
        image_url = res['Remote file_id']
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 保存图片
        img = SKUImage.objects.create(sku_id=sku_id, image=image_url)

        # 更新商品默认显示的图片
        SKU.objects.filter(id=sku_id).update(default_image=image_url)
        # 返回结果
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },
            status=201  # 前端需要接受201状态
        )

    # 重写拓展类的更新业务逻辑
    def update(self, request, *args, **kwargs):

        # 创建FastDFS连接对象
        client = Fdfs_client(settings.FASTDFS_PATH)
        # 获取前端传递的image文件
        data = request.FILES.get('image')
        # 上传图片到fastDFS
        res = client.upload_by_buffer(data.read())
        # 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            return Response(status=403)
        # 获取上传后的路径
        image_url = res['Remote file_id']
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 查询图片对象
        img = SKUImage.objects.get(id=kwargs['pk'])
        # 更新图片
        img.image = image_url
        img.save()
        # 更新商品默认显示的图片
        SKU.objects.filter(id=sku_id).update(default_image=image_url)
        # 返回结果
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },
            status=201  # 前端需要接受201状态码
        )