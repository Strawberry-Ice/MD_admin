from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from meiduo_admin.views.home_views import *
from meiduo_admin.views.user_views import *
from meiduo_admin.views.spu_views import *
from meiduo_admin.views.sku_views import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.image_views import *
from meiduo_admin.views.order_views import *
from meiduo_admin.views.channels_views import *
from meiduo_admin.views.bands_views import *
from meiduo_admin.views.permission_views import *
from meiduo_admin.views.group_views import *
from meiduo_admin.views.admin_views import *
urlpatterns = [
    # url(r'^authorizations/$', LoginView.as_view()),

    url(r'^authorizations/$', obtain_jwt_token),

    url(r'^users/$', UserView.as_view()),

    # SKU表管理
    url(r'^skus/$', SKUGoodsViewSet.as_view({"get": "list", "post": "create"})),

    url(r'^skus/categories/$', SKUCategorieView.as_view()),

    url(r'^goods/simple/$', SPUSimpleView.as_view()),

    url(r'^goods/(?P<pk>\d+)/specs/$', SPUSpecView.as_view()),

    url(r'^skus/(?P<pk>\d+)/$', SKUGoodsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # SPU表管理
    url(r'^goods/$', SPUGoodsViewSet.as_view({"get": "list", "post": "create"})),

    url(r'^goods/brands/simple/$', SPUGoodsViewSet.as_view({"get": "simple"})),

    url(r'^goods/channel/categories/$', SPUGoodsViewSet.as_view({"get": "categories"})),

    url(r'^goods/channel/categories/(?P<pk>\d+)/$', SPUGoodsViewSet.as_view({"get": "channel"})),

    url(r'^goods/(?P<pk>\d+)/$', SPUGoodsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # 规格表
    # url(r'^goods/specs/$', SpecsViewSet.as_view({"get": "list", "post": "create"})),
    #
    # url(r'^goods/specs/(?P<pk>\d+)/$', SpecsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # 选项表
    # url(r'^specs/options/$', OptionsViewSet.as_view({"get": "list", "post": "create"})),
    #
    # url(r'^specs/options/(?P<pk>\d+)/$', OptionsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # 获得新建选项数据的可选规格信息
    url(r'^goods/specs/simple/$', OptionSimpleView.as_view()),

    # 图片表
    # url(r'^skus/images/$', ImageViewSet.as_view({"get": "list", "post": "create"})),

    url(r'^skus/simple/$', ImageViewSet.as_view({"get": "simple"})),

    # url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # 频道表
    # url(r'^goods/channels/$', ChannelsViewSet.as_view({"get": "list", "post": "create"})),

    # url(r'^goods/channels/(?P<pk>\d+)/$', ChannelsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^goods/channel_types/$', ChannelsSimplView.as_view()),

    url(r'^goods/categories/$', GoodsCategoryView.as_view()),

    # 品牌表
    # url(r'^goods/brands/$', BandViewSet.as_view({"get": "list", "post": "create"})),
    # url(r'^goods/brands/(?P<pk>\d+)/$', BandViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # 订单表
    # url(r'^orders/$', OrdersViewSet.as_view({"get": "list"})),

    # url(r'^orders/(?P<pk>\d+)/$', OrdersViewSet.as_view({"get": "retrieve"})),

    url(r'^orders/(?P<pk>\d+)/status/$', OrdersViewSet.as_view({"patch": "status"})),

    # 权限表
    # url(r'^permission/perms/$', PermissionViewSet.as_view({"get": "list"})),

    url(r'^permission/content_types/$', ContentTypeView.as_view()),

    url(r'^permission/simple/$', GroupSimpleView.as_view()),

    url(r'^permission/groups/simple/$', AdminSimpleView.as_view()),
]

router = SimpleRouter()

router.register(prefix='statistical', viewset=HomeViewSet, base_name='home')

# router.register(prefix='skus', viewset=SKUGoodsViewSet, base_name='skus')

router.register(prefix='goods/specs', viewset=SpecsViewSet, base_name='specs')
# 这里注意,goods/(?P<pk>\d+)在映射时DRF中是以(?P<pk>[^/.]+)正则匹配
# router.register(prefix='goods', viewset=SpecsViewSet, base_name='goods')

router.register(prefix='specs/options', viewset=OptionsViewSet, base_name='options')

router.register(prefix='skus/images', viewset=ImageViewSet, base_name='images')

router.register(prefix='goods/channels', viewset=ChannelsViewSet, base_name='channels')

router.register(prefix='goods/brands', viewset=BandViewSet, base_name='brands')

router.register(prefix='orders', viewset=OrdersViewSet, base_name='orders')

router.register(prefix='permission/perms', viewset=PermissionViewSet, base_name='perm')

router.register(prefix='permission/groups', viewset=GroupViewSet, base_name='group')

router.register(prefix='permission/admins', viewset=AdminViewSet, base_name='admin')

urlpatterns += router.urls
