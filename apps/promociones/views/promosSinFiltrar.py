#encoding:utf-8
""" Imports de librerias Django"""
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext


""" Importando la clave (key) de Google Places ademas de las librerias
	necesarias para trabajar con la api.
"""
from django.conf import settings
from googleplaces import GooglePlaces, types, lang, ranking
google_places = GooglePlaces(settings.API_KEY_GOOGLE_PLACES)


""" Importando el modelo Count para contar los datos de una consulta"""
from django.db.models import Count

from datetime import *
hoy = date.today()



""" Importando los modelos a utilizar """
from apps.promociones.models.promocion import Promocion
from apps.usuarios.models.MisCompras import ComprasPasadas
from apps.empresas.models.empresa import Categoria, Empresa


""" 
	La siguiente funcion se va a utilizar para obtener 
	cuales son los Tags que más ha comprado el usuario 
	y se van a regresar por orden de importancia. 
"""
def ContartagsDeCompras(usuario = None):
	compras = ComprasPasadas.objects.filter(us=usuario).order_by('-cantidad')
	return compras

""""
	Esta funcion se utiliza para retornar las catego_
	rias que más compra el usuario y usarlas 
	posteriormente en la llamada a la api de Google
	Places 
"""
def devolverCategorias(usuario=None):
	tags = ContartagsDeCompras(usuario)
	if tags:
		ids_tag_nom =[]
		ids_tag =[]
		for t in tags:
			ide_tag = {'position':t.id,'id_tag':t.tag.id}
			ids_tag_nom.append(t.tag)
			ids_tag.append(ide_tag)
			print "esto es lo que guardo en los tags %s" %(ids_tag_nom)
		cat = Categoria.objects.values('nombre_ingles').filter(
				tags__in=ids_tag_nom).annotate(dcount=Count('nombre_ingles'))
		if cat:
			types_place = []
			for c in cat:
				types_place.append(c['nombre_ingles'])
			return (ids_tag, types_place)
		else:
			types_r = None
			return (ids_tag, types_r)
	else:
		ids = None
		types_r = None
		return (ids, types_r)

"""
	Esta funcion sirve para obtener los tags que más
	ha comprado el usuario ademas de que regresa una lista 
	con las empresas que se encuentran cerca (por orden
	de distancia), solo regresa las empresas que que 
	coninciden con los lugares similares a los que
	ha visitado el usuario
	valores que retorna 
	1) lista 
		a) Lista de los tags que más ha comprado
		b) Lista con los types (tipos de lugares)
		   que ha comprado el usuario.
	2) Empresas que coinciden por lo menos con un
		type (tipo de lugar) que ha comprado el usuario
"""
def regresaPlacesDeInteres(usuario=None,latlon={}):
	ids_t = None
	types_g = None
	ids_t,types_g = devolverCategorias(usuario)
	if ids_t and types_g:
		try:
			query_result = google_places.nearby_search(
						lat_lng=latlon, 
						types=types_g,
						language=lang.SPANISH,
						rankby=ranking.DISTANCE
						)
			ides_t_types_place = {"ids_t":ids_t,"types_g":types_g}
			return (ides_t_types_place,query_result)
		except: 
			query_result= " entro en la exepcion None"
			return (ids_t,query_result)
	else:
		return(None,None)

"""
	Esta fncion sirve para obtener las empresas que 
	son nuestros clientes, que estan cerca y que el usuario
	ha comprado algo relacionado a su giro (Type)
	Datos que retorna 
	1) lista 
		a) Lista de los tags que más ha comprado
		b) Lista con los types (tipos de lugares)
		   que ha comprado el usuario.
	2) Empresas que son nuestros clientes y que le pueden
		gustar al usuario
"""
def verificaEmpresaCliente(usuario=None,latlon={}):
	ides_t_types_place,empresas = regresaPlacesDeInteres(
									usuario,latlon)
	if ides_t_types_place and empresas:
		id_empr = []
		for empr in empresas.places:
			id_empr.append(empr.id)
		if len(id_empr) > 0:
			print id_empr
			empr_clientes = Empresa.objects.filter(
							id_place__in=id_empr)
		return (ides_t_types_place,empr_clientes)

	else:
		return (ides_t_types_place,empresas)


def promocionesGustosClientes(usuario=None,latlon={}):
	ides_t_types_place,empresas = verificaEmpresaCliente(
									usuario,latlon)
	if ides_t_types_place and empresas:
		id_empr = []
		for ids in empresas:
			id_empr.append(ids.id)
		if len(id_empr) > 0:
			promos = Promocion.objects.filter(
					empresa__in=id_empr,
					empresa__is_active__exact=1,
					fecha_publicacion__lte = hoy,
					fecha_termino__gte=hoy)
		if promos:
			for pr in promos:
				dir_cat = []
				for cat in pr.categoria.all():
					dir_cat.append(cat.id)

				print "nombre de la promo: %s, ys su categoria es %s" %(pr.titulo_promocion, dir_cat)
				print ides_t_types_place['ids_t']
				 

#def retornaPosicionTag():








		

