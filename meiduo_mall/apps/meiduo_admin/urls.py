from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from meiduo_admin.views.login_views import LoginView
from meiduo_admin.views.home_views import *
from meiduo_admin.views.user_manage_views import *
from meiduo_admin.views.sku_views import *

urlpatterns = [
    # url(r'^authorizations/$', LoginView.as_view()),

    url(r'^authorizations/$', obtain_jwt_token),

    url(r'^users/$', UserView.as_view()),

    url(r'^skus/$', SKUGoodsView.as_view({"get":"list", "post":"create"})),
    # 获得三级分类信息
    url(r'^skus/categories/$', SKUGoodsView.as_view({"get":"categories"})),
    # 获得SPU信息
    url(r'^goods/simple/$', SKUGoodsView.as_view({"get":"simple"})),


]

router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeViewSet, base_name='home')

urlpatterns += router.urls