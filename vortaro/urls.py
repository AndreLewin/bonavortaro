from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ĉefpaĝo, name='ĉefpaĝURLo'),
    url(r'^(?P<URLeraro>.+)/$', views.radikpaĝo, name='radikpaĝURLo'),
]