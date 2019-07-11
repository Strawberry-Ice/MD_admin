from django.utils import timezone
from django.conf import settings
import pytz


# 获取当日的零时
# .now()--年月日时分秒
# .date()--年月日
# timezone.now()-->当前时间(上海时区)

def obtain_zero_shanghai():
    date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE))
    date_zero_shangha = date.replace(hour=0, minute=0, second=0)
    return date_zero_shangha
