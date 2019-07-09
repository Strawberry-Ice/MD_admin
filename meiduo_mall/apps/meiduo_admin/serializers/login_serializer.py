from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler


# 定义序列化器
# 业务流程: 对用户密码校验, 签发token值

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



    def validate(self, attrs):

        user = authenticate(**attrs)

        if not user:
            # 认证失败
            raise serializers.ValidationError('用户名或密码错误!')

        # 认证通过
        payload = jwt_payload_handler(user)
        jwt_token = jwt_encode_handler(payload)

        return {
            "user": user,
            "token": jwt_token
        }


