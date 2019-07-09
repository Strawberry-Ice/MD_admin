from django.conf.urls import url
from meiduio_admin.views.login_views import LoginView

urlpatterns = [
    url(r'^authorizations/$', LoginView.as_view()),
]