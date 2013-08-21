#encoding:utf-8
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
	url(r'^ajax/selectestado/(?P<id_estado>\d+)$', 'apps.empresas.views.actualizarDatos.selectMunicipios',name='busca_municios'),
	url(r'^ajax/selectlocalidad/(?P<id_municipio>\d+)$', 'apps.empresas.views.actualizarDatos.selectLocalidades',name='busca_localidades'),
)