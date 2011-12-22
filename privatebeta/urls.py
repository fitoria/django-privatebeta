from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'privatebeta.views.invite', name='privatebeta_invite'),
    url(r'^activate/(?P<code>\w+)/$', 'privatebeta.views.activate_invite',
        {'redirect_to': '/register/'}, name='privatebeta_activate_invite'),
    url(r'^sent/$', 'privatebeta.views.sent', name='privatebeta_sent'),
)
