#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
""" la siguiente linea se agrega para poder utilizar la ruta de los archivos
  estatic se debe poner en todas las funciones """
from django.template import RequestContext

from django.contrib.auth.models import User

""" Importando los modelos a utilizar """
from apps.promociones.models.promocion import Promocion
from apps.comentarios.models.comentario import Comentario_promocion
from apps.cupones.models.cupon import Cupon

""" Importando todos los formularios que se van a utilizar """
from apps.comentarios.forms.comentarios import ComentarPromocionForm


def MostrarPromocionCompleta(request, dni_promo = 1 ):
	promocion = ""
	cupones_usuario =""
	formulario_comentario = ""
	formlarioGuardado = False

	try:
		promocion_detalle = Promocion.objects.get(pk=dni_promo)
		comentarios_promocion = Comentario_promocion.objects.filter(
									promocion = promocion_detalle)
		cupones_usuario = Cupon.objects.get(
									pk=dni_promo,usuario=request.user.id)
		print "realizo todas las consultas "
		if cupones_usuario.canjeado == False:
			if request.method == 'POST':
				print "entro en el metodo post "
				formulario_comentario = ComentarPromocionForm(request.POST)
				if formulario_comentario.is_valid():
					aux = formulario_comentario.save(commit=False)

					""" estas son las instrucciones correctas, pero creo
					que no me las acepta por que no se estan manejando seciones
					por eso las pongo mas abajo de forma estatica, pero lo mas 
					probable es que se hagan por medio de ajax y no de esta
					forma, lo pongo para ver el funcionamiento """
					#aux.usuario = request.user.id
					#aux.promocion =  dni_promo


					#Las siguientes dos lineas no sirven son estaticas!!!!
					us = User.objects.get(pk=3)
					aux.usuario = us
					aux.promocion =  Promocion.objects.get(pk=2)
					#revisar que pasa si la promocion no existe
					aux.save()
					promo_canjeada = Cupon.objects.filter(pk=2,usuario=us).update(canjeado=True)
					if promo_canjeada:
						print "si se guardo la promo canjeada"
					
					
					formlarioGuardado = True
			if formlarioGuardado == False:
				formulario_comentario = ComentarPromocionForm()
		else: 
			formlarioGuardado = True

		#Cambiar el numero 3 por request.user.id 
		print cupones_usuario
		print comentarios
		print promocion
		print request.user.id
	except Exception, e:
		mensaje = "no existe la promocion"
	finally:
		ctx = {'promocion':promocion_detalle,'formulario':formulario_comentario,
				'comentarios':comentarios_promocion,'cup':formlarioGuardado}
		return render_to_response('promociones/detalle_promocion.html',
				ctx,context_instance=RequestContext(request))