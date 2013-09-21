from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^agregaComentario/$', 'apps.comentarios.views.agregaComentario'),
    url(r'^indexComentarios/$', 'apps.comentarios.views.indexComentarios'),
    url(r'^eliminaComentario/$', 'apps.comentarios.views.eliminaComentario'),
    url(r'^modificarComentario/$', 'apps.comentarios.views.modificarComentario'),
    url(r'^calificarComentario/$', 'apps.comentarios.views.calificarComentario'),
    url(r'^leerComentarios/$', 'apps.comentarios.views.leerComentarios'),
)