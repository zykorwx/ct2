#encoding:utf-8

""" Importar modelos a utilizar """

from apps.empresas.models.empresa import Empresa, Categoria
from apps.comentarios.models.preguntas import Preguntas_promocion,Calificacion_promocion

""" Importando las librerias python a utilizar """
import json
from django.core import serializers 

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