from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	 url(r'', include('social_auth.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'usuarios/login.html'}),
    url(r'^cerrarSesion/$', 'usuarios.views.cerrarSesion'),
	url(r'^registroEmpresa/$', 'usuarios.views.nuevaEmpresaView'), # agregar nueva empresa
	url(r'^registroUsuario/$', 'usuarios.views.nuevoConsumidorView'), # agregar nuevo usuario
    # Examples:
    url(r'^$', 'usuarios.views.index', name='home'),
    url(r'^logeado/$', 'usuarios.views.logeado', name='Logeado'),
)