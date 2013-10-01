#encoding:utf-8

""" Importar modelos a utilizar """

from apps.empresas.models.empresa import Empresa, Categoria
from apps.promociones.models.promocion import Promocion
from apps.comentarios.models.preguntas import Preguntas_promocion,Calificacion_promocion

""" Importando las librerias python a utilizar """
import json
from django.core import serializers 
from django.db import IntegrityError, transaction

def buscaPreguntas(data = None):
	data = json.loads(data)
	empresa = None
	categoria =  None
	try:
		if data.has_key("empresa"):
			empresa =  Empresa.objects.get(pk=data["empresa"])
		else:
			resultado = {"error":"CO-0000548"}
	except Empresa.DoesNotExist:
		resultado = {"error":"CO-0000550"}
	except Exception, e:
		a = "no se que paso"
	

	if empresa:
		categoria = empresa.giro
		if categoria:
			try:
				preguntas = Preguntas_promocion.objects.filter(categoria = categoria)
				if preguntas:
					resultado = {"transaccion":"efectiva","preguntas":serializers.serialize('json', preguntas)}
				else:
					resultado = {"error":"CO-0000549"}
			except Exception, e:
				raise
	return json.dumps(resultado)

#El sigiente es el json (ejemplo que voy a recibir)
#data={"user":user,"promocion":222222,"preguntas":{1222:55,1222:5,1244:55,1:4,2:3,3:4,4:4}}
def agregarCalificacion(data= None):
	us = None
	promo = None
	resultado = {}
	if data:
		data =  json.loads(data)
		if data.has_key("user") and data.has_key("promocion"):
			us =  data["user"]
			promo = data["promocion"]
			preguntas = data["preguntas"]
			agrega = addCalenBd(us,promo,preguntas)
			if agregar:
				resultado = {"transaccion":"exitosa"}
			else:
				resultado = {"transaccion":"fallida"}
	else:
		resultado = {"error":"CO-0000551"}


	return json.dumps(resultado)


#@transaction.atomic
def addCalenBd(user=None,promo=None,preguntas=None):
	realizado = False
	if user and promo and preguntas:
		for x in preguntas.keys():
			try:
				Calificacion_promocion.objects.create(
						promocion_id=promo,
						pregunta_id=x,
						usuario_id=user,
						calificacion=preguntas[x])
				realizado = True
			except Exception, e:
				realizado =  False
				raise		
	#do_stuff()
	return realizado

