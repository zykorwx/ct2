#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect
from django.db import DatabaseError, IntegrityError
from apps.comentarios.models import Comentario_promocion
from django.core import serializers
import json


# Eliminar despues de terminar junto con el template
def indexComentarios(request):
	if request.user.is_authenticated():
		return render_to_response('pruebas/comentarios.html', context_instance=RequestContext(request))


def leerComentarios(request):
	if request.user.is_authenticated():
		if (request.GET != {}):
			try:
				auxDatos = request.GET
				comentarios = Comentario_promocion.objects.get(promocion_id=int(auxDatos['id_promocion']))
				auxComentarios = json.loads(comentarios.comentarios)
				return HttpResponse(json.dumps({"comentarios": auxComentarios}), content_type="application/json")					
			except DatabaseError as e:
				return HttpResponse(json.dumps({"error": "database error"}), content_type="application/json")					
			except IntegrityError as e:
				return HttpResponse(json.dumps({"error": "integridad"}), content_type="application/json")	
			except Comentario_promocion.DoesNotExist:
				return HttpResponse(json.dumps({"error": "Sin resultados"}), content_type="application/json")	
		else:
			return HttpResponse(json.dumps({"error": "No he recibido informacion"}), content_type="application/json")
	else:
		return redirect('/')


# Este es para registrar una nueva empresa
def agregaComentario(request):
	if request.user.is_authenticated():
		if (request.GET != {}):
			try:
				auxDatos = request.GET
				comentario, auxBool = Comentario_promocion.objects.get_or_create(promocion_id=int(auxDatos['id_promocion']))
				if (auxBool == True):
					if (primerComentarioPromocion(comentario, request.user.pk, request.user.first_name, request.user.last_name, auxDatos) == True):
						return HttpResponse(json.dumps({"exito": "Se ha guardado tu comentario"}), content_type="application/json")
					else:
						return HttpResponse(json.dumps({"error": "No se ha guardado tu comentario"}), content_type="application/json")
				else:
					if (agregaComentarioPromocion(comentario, request.user.pk, request.user.first_name, request.user.last_name, auxDatos) == True):
						return HttpResponse(json.dumps({"exito": "Se ha guardado tu comentario"}), content_type="application/json")
					else:
						return HttpResponse(json.dumps({"error": "No se ha guardado tu comentario"}), content_type="application/json")					
			except DatabaseError as e:
				return HttpResponse(json.dumps({"error": "database error"}), content_type="application/json")					
			except IntegrityError as e:
				return HttpResponse(json.dumps({"error": "integridad"}), content_type="application/json")		
		else:
			return HttpResponse(json.dumps({"error": "No he recibido informacion"}), content_type="application/json")
	else:
		return redirect('/')
	
""" ATENCION: SE TIENE QUE VALIDAR QUE LA ENTRADA NO CONTENGA COMILLAS DOBLES SI NO TRONARA, SE PUEDEN ACEPTAR COMILLAS SIMPLES 
    La Validacion si el usuario ya ha comentado se realizara del lado del usuario   """
# Este metodo se ejecuta cuando es el primer comentario de la promocion
def primerComentarioPromocion(comentario, user_id,  first_name, last_name, auxDatos):
	try:
		from time import gmtime, strftime
		auxTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		auxNewComentario = u'{"comentarios": [{"usuario": {"id": %s, "nombre": "%s %s" },"datetime": "%s","titulo": "%s","comentario": "%s",\
			"calificaciones":[]}]}' %\
			(user_id, first_name, last_name, auxTime, auxDatos["titulo"], auxDatos["comentario"])
		comentario.comentarios = auxNewComentario;
		comentario.save()
		return True;
	except DatabaseError as e:
		print e
	except IntegrityError as e:
		print e

# Este metodo agrega el comentario en el json ya existente
def agregaComentarioPromocion(comentario, user_id,  first_name, last_name, auxDatos):
	try:
		from time import gmtime, strftime
		auxTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		auxNewComentario = '{"usuario": {"id": %s, "nombre": "%s %s" }, "datetime": "%s","titulo": "%s", "comentario": "%s", "calificaciones": []}' %\
			(user_id, first_name, last_name, auxTime, auxDatos["titulo"], auxDatos["comentario"])
		nuevo = json.loads(auxNewComentario)
		comentariosObj = json.loads(comentario.comentarios)
		comentariosObj["comentarios"].append(nuevo)
		comentario.comentarios = json.dumps(comentariosObj)
		comentario.save()
		return True;
	except DatabaseError as e:
		print e
	except IntegrityError as e:
		print e


# Este es para registrar una nueva empresa
def eliminaComentario(request):
	if request.user.is_authenticated():
		if (request.GET != {}):
			try:
				auxDatos = request.GET
				comentario = Comentario_promocion.objects.get(promocion_id=int(auxDatos['id_promocion']))
				comentariosObj = json.loads(comentario.comentarios)
				comentariosObj["comentarios"].pop(int(auxDatos['index']))
				comentario.comentarios = json.dumps(comentariosObj)
				comentario.save()
				return HttpResponse(json.dumps({"exito": "Se ha eliminado tu comentario"}), content_type="application/json")			
			except DatabaseError as e:
				return HttpResponse(json.dumps({"error": "database error"}), content_type="application/json")					
			except IntegrityError as e:
				return HttpResponse(json.dumps({"error": "integridad"}), content_type="application/json")
			except Comentario_promocion.DoesNotExist:
				return HttpResponse(json.dumps({"error": "Sin resultados"}), content_type="application/json")	
		else:
			return HttpResponse(json.dumps({"error": "No he recibido informacion"}), content_type="application/json")
	else:
		return redirect('/')


# Este es para registrar una nueva empresa
def modificarComentario(request):
	if request.user.is_authenticated():
		if (request.GET != {}):
			try:
				from time import gmtime, strftime
				auxTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
				auxDatos = request.GET
				comentario = Comentario_promocion.objects.get(promocion_id=int(auxDatos['id_promocion']))
				comentariosObj = json.loads(comentario.comentarios)
				comentariosObj["comentarios"][int(auxDatos['index'])]['datetime'] = auxTime
				comentariosObj["comentarios"][int(auxDatos['index'])]['titulo'] = auxDatos['titulo']
				comentariosObj["comentarios"][int(auxDatos['index'])]['comentario'] = auxDatos['comentario']
				comentario.comentarios = json.dumps(comentariosObj)
				comentario.save()
				return HttpResponse(json.dumps({"exito": "Se ha actualizado tu comentario"}), content_type="application/json")			
			except DatabaseError as e:
				return HttpResponse(json.dumps({"error": "database error"}), content_type="application/json")					
			except IntegrityError as e:
				return HttpResponse(json.dumps({"error": "integridad"}), content_type="application/json")
			except Comentario_promocion.DoesNotExist:
				return HttpResponse(json.dumps({"error": "Sin resultados"}), content_type="application/json")		
		else:
			return HttpResponse(json.dumps({"error": "No he recibido informacion"}), content_type="application/json")
	else:
		return redirect('/')

# Este es para registrar una nueva empresa
def calificarComentario(request):
	if request.user.is_authenticated():
		if (request.GET != {}):
			try:
				auxDatos = request.GET
				comentario = Comentario_promocion.objects.get(promocion_id=int(auxDatos['id_promocion']))
				comentariosObj = json.loads(comentario.comentarios)
				if ( len(comentariosObj["comentarios"][int(auxDatos['index'])]['calificaciones'])  == 0):
					auxCalificacionComentario = json.loads('{"id_user": %s , "calificacion": %s}' % (request.user.pk, int(auxDatos["calificacion"])))
					comentariosObj["comentarios"][int(auxDatos['index'])]['calificaciones'].append(auxCalificacionComentario)
					comentario.comentarios = json.dumps(comentariosObj)
					comentario.save()
					return HttpResponse(json.dumps({"exito": "Calificacion aplicada lentgth == 0"}), content_type="application/json")
				else:
					auxIndex = -1
					for i in range(len(comentariosObj["comentarios"][int(auxDatos['index'])]['calificaciones'])):
						if (comentariosObj["comentarios"][int(auxDatos['index'])]['calificaciones'][i]['id_user'] == request.user.pk):
							print i
							auxIndex = i
							break
					if auxIndex != -1:
						# En caso de que el usuario ya haya comentado solo se le actualizara su comentario
						print auxIndex
						auxCalificacionComentario = json.loads('{"id_user": %s , "calificacion": %s}' % (request.user.pk, int(auxDatos["calificacion"])))
						comentariosObj["comentarios"][int(auxDatos['index'])]['calificaciones'][auxIndex] = auxCalificacionComentario
						comentario.comentarios = json.dumps(comentariosObj)
						comentario.save()
						return HttpResponse(json.dumps({"exito": "Calificacion aplicada auxIndex != -1"}), content_type="application/json")
					else:
						# En caso de que existan otros comentarios pero ninguno mio xD
						print auxIndex
						auxCalificacionComentario = json.loads('{"id_user": %s , "calificacion": %s}' % (request.user.pk, int(auxDatos["calificacion"])))
						comentariosObj["comentarios"][int(auxDatos['index'])]['calificaciones'].append(auxCalificacionComentario)
						comentario.comentarios = json.dumps(comentariosObj)
						comentario.save()
						return HttpResponse(json.dumps({"exito": "Calificacion aplicada auxIndex == -1 "}), content_type="application/json")
			except DatabaseError as e:
				return HttpResponse(json.dumps({"error": "database error"}), content_type="application/json")					
			except IntegrityError as e:
				return HttpResponse(json.dumps({"error": "integridad"}), content_type="application/json")
			except Comentario_promocion.DoesNotExist:
				return HttpResponse(json.dumps({"error": "Sin resultados"}), content_type="application/json")		
		else:
			return HttpResponse(json.dumps({"error": "No he recibido informacion"}), content_type="application/json")
	else:
		return redirect('/')