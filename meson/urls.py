from django.conf.urls import patterns, url

from meson import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^menuPermanent/$', views.menuPermanent, name='menuPermanent'),
    url(r'^menuDaily/$', views.menuDaily, name='menuDaily'),
    url(r'^events/$', views.events, name='events'),
    url(r'^booking/$', views.booking, name='booking'),
    url(r'^contact/$', views.contact, name='contact'),
)
