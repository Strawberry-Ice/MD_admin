from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import User
from django.utils import timezone


class HomeViewSet(ViewSet):

    # 获取用户总数
    # GET
    # statistical/total_count/
    @action(methods=['get'], detail=False)
    def total_count(self, request):
        count = User.objects.count()

        date = timezone.now().date()

        return Response({
            'count': count,
            'date': date
        })