from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^indexInvitaciones/$', 'apps.invitaciones.views.indexInvitaciones'),
)