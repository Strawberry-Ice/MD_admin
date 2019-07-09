from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from meiduo_admin.serializers.login_serializer import *


class LoginView(APIView):

    def post(self, request):
        # 使用序列化器实现用户传统登录, token签发
        # 1. 构建序列化器对象
        s = LoginSerializer(data=request.data)
        # 2. 数据校验
        s.is_valid(raise_exception=True)
        # 3.序列化返回
        return Response({
            "username": s.validated_data['user'].username,
            "user_id": s.validated_data['user'].id,
            "token": s.validated_data['token'],
        })
