from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'usuarios/login.html'}),
    url(r'^cerrarSesion/$', 'apps.usuarios.views.cerrarSesion'),
	url(r'^registroEmpresa/$', 'apps.usuarios.views.nuevaEmpresaView'), # agregar nueva empresa
	url(r'^registroUsuario/$', 'apps.usuarios.views.nuevoConsumidorView'), # agregar nuevo usuario
    # Examples:
    url(r'^$', 'apps.usuarios.views.index', name='home'),
    url(r'^logeado/$', 'apps.usuarios.views.logeado', name='Logeado'),
)