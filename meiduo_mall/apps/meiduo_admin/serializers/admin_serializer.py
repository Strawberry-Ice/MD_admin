from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import Group
from users.models import User


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # 重写父类方法
    def create(self, validated_data):
        # 1
        # groups = validated_data.pop('groups') # [1,2,3...]
        # user_permissions = validated_data.pop('user_permissions') # [9,7,6]
        #
        # # instance是主表对象
        # instance = User.objects.create_superuser(**validated_data)
        #
        # # instance.id --> 12
        # # user_group:   12   1
        # #               12   2
        # #               12   3
        # instance.groups.set(groups)
        # instance.user_permissions.set(user_permissions)
        # instance.save()
        #
        # return instance

        # 2
        # validated_data['password'] = make_password(validated_data['password'])
        # validated_data['is_staff'] = True
        # return super().create(validated_data)

        # 3
        # 添加管理员字段
        validated_data['is_staff'] = True
        # 调用父类的方法创建管理员用户
        admin = super().create(validated_data)
        # 密码加密
        password = validated_data['password']
        admin.set_password(password)
        admin.save()
        return admin

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)