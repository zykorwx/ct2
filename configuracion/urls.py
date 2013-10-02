#encoding:utf-8
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ct2.views.home', name='home'),
    # url(r'^ct2/', include('ct2.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #Urls para las calificaciones
    url(r'^promo/detalle/(?P<dni_promo>\d+)$', 
    	'apps.promociones.views.mostrar_promo.MostrarPromocionCompleta',
    	name='detalle_promocion'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('apps.usuarios.urls.urls')),
    url(r'', include('apps.empresas.urls.urls')),
    url(r'', include('apps.comentarios.urls')),
    url(r'', include('apps.invitaciones.urls')),

)


# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
