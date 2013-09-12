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
def devolverCategorias(usuario=None,gustos= True):
	tags = ContartagsDeCompras(usuario)
	if tags:
		ids_tag_nom =[]
		ids_tag =[]
		contador = 1
		for t in tags:
			###ide_tag = {'position':contador,'id_tag':t.tag.id}
			contador += 1
			ids_tag_nom.append(t.tag)
			ids_tag.append(t.tag.id)
		print ids_tag
			###print "esto es lo que guardo en los tags %s" %(ids_tag_nom)
		if gustos:
			cat = Categoria.objects.values('nombre_ingles').filter(
				tags__in=ids_tag_nom).annotate(dcount=Count('nombre_ingles'))
		else:
			cat = Categoria.objects.values(
				'nombre_ingles').all().exclude(
				tags__in=ids_tag_nom).annotate(
				cantidad=Count('nombre_ingles'))
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
### en mi pc de escritorio hayq ue cambiar google_places.query(
### por  por la siguiente linea   ::::::: google_places.nearby_search(
def regresaPlacesDeInteres(usuario=None,latlon={}, dis_metros=None, gustos=True):
	ids_t = None
	types_g = None
	ids_t,types_g = devolverCategorias(usuario,gustos)
	print " no se que paso peroe esta antes del google places query"

	if ids_t and types_g:
		if dis_metros:
			query_result = google_places.query(
							lat_lng=latlon,
							types=types_g,
							language=lang.SPANISH,
							radius=dis_metros)
		else:
			query_result = google_places.query(
							lat_lng=latlon,
							types=types_g,
							language=lang.SPANISH,
							rankby= ranking.DISTANCE)
		
		print query_result
		ides_t_types_place = {"ids_t":ids_t,"types_g":types_g}
		return (ides_t_types_place,query_result)
	
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
def verificaEmpresaCliente(usuario=None,latlon={}, dis_metros=None, gustos=True):
	ides_t_types_place,empresas = regresaPlacesDeInteres(
									usuario,latlon, dis_metros,gustos)

	if ides_t_types_place and empresas:
		id_empr = []
		for empr in empresas.places:
			id_empr.append(empr.id)
		if len(id_empr) > 0:
			###print id_empr
			empr_clientes = Empresa.objects.filter(
							id_place__in=id_empr)
			dicc_posision = {}
			for inde in empr_clientes:
				pos = id_empr.index(inde.id_place)
				dicc_posision[inde.id] = pos

			dic_emp_position = {"empresa" : empr_clientes, "position" : dicc_posision}

		return (ides_t_types_place,dic_emp_position)

	else:
		return (None,None)



"""
	Esta es la funcion principal, es la que se va a invocar en las vistas para que regrese todo 
	el contenido. regresa una lista de diccionarios y cada diccionario trae 
	1)n objeto de tipo promocion, ya filtrada por los gustos del usuario, que la promo-
	  ción este activa (por las fechas de pub) que la empresa este activa
	2) posicion en la que debe ir segun la distancia
	3) posición en la que debe ir según los gustos del usuario.
	4) tag de la promocion para poder organizar rapidamente las promos por tag.
"""

def promocionesGustosClientes(usuario=None,latlon={}, dis_metros=None, gustos=True):
	ides_t_types_place,empresas = verificaEmpresaCliente(
									usuario,latlon,dis_metros,gustos)
	if ides_t_types_place and empresas:
		id_empr = []
		for ids in empresas['empresa']:
			id_empr.append(ids.id)
		if len(id_empr) > 0:
			promos = Promocion.objects.filter(
					empresa__in=id_empr,
					empresa__is_active__exact=1,
					fecha_publicacion__lte = hoy,
					fecha_termino__gte=hoy)
		if promos:
			promos_ordenadas = []
			###print ides_t_types_place['ids_t']
			for pr in promos:
				dir_cat = []
				dis = empresas['position'][pr.empresa.id]
				for cat in pr.categoria.all():
					aux1 = verificaPosisionTag(ides_t_types_place['ids_t'],cat.id)
					print "esto trae aux %s" % (aux1)
					if aux1:
						pos = {'posision':aux1,'tag_nom':cat.nombre,'tag_id': cat.id}
						###print pos
						dir_cat.append(pos)
					if len(dir_cat) > 0 and aux1:
						if dir_cat[0]['posision'] > aux1:
							dir_cat[0]['posision'] = aux1
							dir_cat[0]['tag_nom'] = cat.nombre
							dir_cat[0]['tag_id'] = cat.id
				print dir_cat
					

				env_promos = {'posision_gusto':dir_cat[0]['posision'],'promo': pr,'tag' : dir_cat[0]['tag_nom'],'lugar_empresa':dis}
				promos_ordenadas.append(env_promos)



				###print "nombre de la promo: %s, ys su categoria es %s" %(pr.titulo_promocion, dir_cat)
				###print ides_t_types_place['ids_t']
			return promos_ordenadas


def verificaPosisionTag(tags=[],id_tag = -1):
	
	
	if id_tag in tags:
		print "la  categoria %s la encontro  en el indice numero  %s" %(id_tag, tags.index(id_tag) + 1) 
		return tags.index(id_tag) + 1
	else:
		return None

				 

#def retornaPosicionTag():








		

