from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'usuarios/login.html'}),
    url(r'^cerrarSesion/$', 'apps.usuarios.views.cerrarSesion'),
	url(r'^registroEmpresa/$', 'apps.usuarios.views.nuevaEmpresaView'), # agregar nueva empresa
	url(r'^registroUsuario/$', 'apps.usuarios.views.nuevoConsumidorView'), # agregar nuevo usuario
    # Examples:
    url(r'^$', 'apps.usuarios.views.index', name='home'),
    url(r'^logeado/$', 'apps.usuarios.views.logeado', name='Logeado'),
    url(r'^empresa/$', 'apps.usuarios.views.logeoEmpresa'),
    url(r'^vincular/(?P<facebook_uid>\d+)$', 'apps.usuarios.views.vinculaCuentaXFacebook'),
    url(r'^vinculaCuentaXEmpresa/(?P<empresa_id>\d+)$', 'apps.usuarios.views.vinculaCuentaXEmpresa'),
	url(r'^confirm/(?P<empresa_id>\d+)/(?P<codigo>[\w]{32})/$', 'apps.usuarios.views.confirm', name='user_confirm'),
)