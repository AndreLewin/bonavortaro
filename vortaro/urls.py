from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ĉefpaĝo, name='ĉefpaĝURLo'),
    url(r'^nova_radiko$', views.aldonpaĝo, name='aldonpaĝURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/forigi/$', views.radikforigo, name='radikforigURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/nova_propono/$', views.proponaldono, name='proponaldonURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/pori/$', views.radikporo, name='radikporURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/malpori/$', views.radikmalporo, name='radikmalporURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/(?P<proponURLeraro>[^\/]+)/pori/$', views.proponporo, name='proponporURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/(?P<proponURLeraro>[^\/]+)/malpori/$', views.proponmalporo, name='proponmalporURLo'),

    url(r'^(?P<radikURLeraro>[^\/]+)/(?P<proponURLeraro>[^\/]+)/forigi/$', views.proponforigo, name='proponforigURLo'),
    url(r'^(?P<radikURLeraro>[^\/]+)/$', views.radikpaĝo, name='radikpaĝURLo'),
    # TODO : Trovi kial radikpaĝoj ne plu funkcias
]