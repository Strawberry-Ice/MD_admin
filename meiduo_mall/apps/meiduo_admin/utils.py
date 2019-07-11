from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils import timezone
from django.conf import settings
import pytz


# 获取当日的零时
# .now()--年月日时分秒
# .date()--年月日
# timezone.now()-->当前时间(上海时区)


# 获取当日零时
def obtain_zero_shanghai():
    date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE))
    date_zero_shangha = date.replace(hour=0, minute=0, second=0)
    return date_zero_shangha


# 分页器
class UserPageNum(PageNumberPagination):
    page_size = 5  # 每页显示数量
    page_size_query_param = 'pagesize'
    max_page_size = 10  # 最大页数

    # 重写分页返回方法，按照指定的字段进行分页数据返回
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,  # 总数量
            'lists': data,  # 用户数据
            'page': self.page.number,  # 当前页数
            'pages': self.page.paginator.num_pages,  # 总页数
            'pagesize': self.page_size  # 后端指定的页容量
        })