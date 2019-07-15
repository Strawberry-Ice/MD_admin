from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from meiduo_admin.views.login_views import LoginView
from meiduo_admin.views.home_views import *
from meiduo_admin.views.user_views import *
from meiduo_admin.views.spu_views import *
from meiduo_admin.views.sku_views import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.image_views import *
from meiduo_admin.views.order_views import *
from meiduo_admin.views.channels_views import *

urlpatterns = [
    # url(r'^authorizations/$', LoginView.as_view()),

    url(r'^authorizations/$', obtain_jwt_token),

    url(r'^users/$', UserView.as_view()),
    # SKU表管理
    url(r'^skus/$', SKUGoodsView.as_view({"get": "list", "post": "create"})),

    url(r'^skus/categories/$', SKUCategorieView.as_view()),

    url(r'^goods/simple/$', SPUSimpleView.as_view()),

    url(r'^goods/(?P<pk>\d+)/specs/$', SPUSpecView.as_view()),

    url(r'^skus/(?P<pk>\d+)/$', SKUGoodsView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # SPU表管理
    url(r'^goods/$', SPUGoodsViewSet.as_view({"get": "list", "post": "create"})),

    url(r'^goods/brands/simple/$', SPUGoodsViewSet.as_view({"get": "simple"})),

    url(r'^goods/channel/categories/$', SPUGoodsViewSet.as_view({"get": "categories"})),

    url(r'^goods/channel/categories/(?P<pk>\d+)/$', SPUGoodsViewSet.as_view({"get": "channel"})),

    url(r'^goods/(?P<pk>\d+)/$', SPUGoodsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^goods/specs/$', SpecsView.as_view({"get": "list", "post": "create"})),

    url(r'^goods/specs/(?P<pk>\d+)/$', SpecsView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^specs/options/$', OptionsView.as_view({"get": "list", "post": "create"})),

    url(r'^goods/specs/simple/$', OptionSimpleView.as_view()),

    url(r'^specs/options/(?P<pk>\d+)/$', OptionsView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^skus/images/$', ImageView.as_view({"get": "list", "post": "create"})),

    url(r'^skus/simple/$', ImageView.as_view({"get": "simple"})),

    url(r'^skus/images/(?P<pk>\d+)/$', ImageView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^goods/channels/$', ChannelsViewSet.as_view({"get": "list"})),

    url(r'^orders/$', OrdersView.as_view({"get": "list"})),

]

router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeViewSet, base_name='home')
# router.register(prefix='goods', viewset=SPUGoodsViewSet, base_name='spu')

urlpatterns += router.urls
