from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ĉefpaĝo, name='ĉefpaĝURLo'),
    url(r'^nova_radiko$', views.aldonpaĝo, name='aldonpaĝURLo'),
    url(r'^(?P<URLeraro>[^\/]+)/forigi/$', views.radikforigo, name='radikforigURLo'),
    url(r'^(?P<URLeraro>[^\/]+)/nova_propono/$', views.proponaldono, name='proponaldonURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/pori/$', views.radikporo, name='radikporURLo'),

    url(r'^(?P<radikURLeraro>[^\/]+)/(?P<proponURLeraro>[^\/]+)/forigi/$', views.proponforigo, name='proponforigURLo'),
    url(r'^(?P<URLeraro>[^\/]+)/$', views.radikpaĝo, name='radikpaĝURLo'),
]