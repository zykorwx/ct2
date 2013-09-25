# -*- coding: utf-8 *-*
""" 
	Importando los modelos a utilizar 
"""	
from apps.promociones.models.promocion import Promocion
from apps.cupones.models.cupon import Cupon
from apps.pagos.models import cobroCuponComision
from apps.empresas.models.empresa import Empresa
from apps.usuarios.models.MisCompras import ComprasEmpresaFavorita
from apps.usuarios.models.perfil import userTarjeta

from django.contrib.auth.models import User


from apps.promociones.views.porcentajeComisionPromo import *

from django.db.models import  Sum
import json
import json as simplejson
from django.core import serializers 

import re
import decimal
from decimal import *



def contarComprasEmpresasMatriz(empresas = None,user=None):
	compras = None
	if empresas:
		compras = ComprasEmpresaFavorita.objects.filter(
					empresa__in=empresas,us=user).aggregate(
					total=Sum('cantidad'))
	return compras

def obtenerMiDescuento(empresa = None,user=None,descuento = 5):
	resul =  None
	buscaMatriz = empresa.matriz
	totalCompras = 0
	if buscaMatriz:
		empresasFranquicia = Empresa.objects.filter(matriz=buscaMatriz)
		if empresasFranquicia:
			mis_compras = contarComprasEmpresasMatriz(empresasFranquicia,user)
			if mis_compras:
				totalCompras = mis_compras['total']
	else:
		mis_compras =  ComprasEmpresaFavorita.objects.filter(
						empresa=empresa,us=user)
		if mis_compras:
			for aux in mis_compras:
				totalCompras = aux.cantidad
	
	if totalCompras <= Preferente:
		resul ={'pre':descuento} 
	elif totalCompras <= Platino:
		resul ={'pla':descuento + aumentoDescuento} 
		
	elif totalCompras <= Golden:
		resul ={'gol':descuento + (aumentoDescuento * 2)} 
	else:
		resul ={'pmi':descuento + (aumentoDescuento * 3)} 
	return resul
"""

def obtenerComprasEmpresa(empresa = None,user=None,descuentoInicial = 5):
	cantidad = 0
	descuento = descuentoInicial
	membresia ='pre'
	compras =  ComprasEmpresaFavorita.objects.filter(
				empresa=empresa,us=user)
	if compras:
		for aux in compras:
			cantidad = aux.cantidad
	if cantidad < 6:
		descuento = descuento
	elif cantidad < 11:
		membresia ='pla'
		descuento += 5
	elif cantidad < 16:
		membresia ='gol'
		descue += 10
	else:
		membresia ='pmi'
		descuento += 15
	return (membresia,descuento)
	
	
def verificaDescuentoMiembro(desMiembros = None,miembro=None,descuento = None,
								costoPromocion=None,empresa = None,cupon=None,
								empleado = None):
	if miembro = 'pre':
		if desMiembros['pre']['i'] > desMiembros['pre']['a']:
			capitalEmpresa = empresa.total_capital
			if costoPromocion and descuento:
				comisionPromo = costoPromocion * descuento
				if capitalEmpresa > comisionPromo:
					
					try:
						empresa.total_capital -= comisionPromo
						empresa.save()
						desMiembros['pre']['a'] += 1
						cupon.tipo_user_tarjeta = {'pre':descuento}
						cupon.fecha_canjeado = date.today()
						if empleado:
							cupon.empleado_atend = empleado
						cupon.save()



					except Exception, e:
						raise
					else:
						pass
					finally:
						pass
					








def verificaCobro(promocion = None,cupon= None,user=None):
	if promocion and cupon and user:
		costo = promocion.precio_total
		
		cantidadDescuentos = promocion.tiposDescuentos
		empresa =  promociones.empresa
		matriz = empresa.matriz
		descuentoInicial = promocion.descuento
		if matriz:
			membresia,descuentoUser = obtenerComprasMatriz(
											matriz,user,descuentoInicial)
		else:
			empresa = promociones.empresa
			membresia,descuentoUser = obtenerComprasEmpresa(
											empresa,user,descuentoInicial)


def cobrarComisionPromocion(promocion = None,cupon= None):
	if promocion and cupon:
		costoPromo = promocion.precio_total
		descuentoUser = cupon.tipo_user_tarjeta
		empresa =  promociones.empresa
		capitalEmpresa = empresa.total_capital
		comisionPromo = costoPromo * porcentajeComision
				if capitalEmpresa > comisionPromo:
"""
"""
	Crear el modulo que se va a utilizar cuando un usuario solicite una 
	promocion, voy a recibir como datos de entrada
	1) id_User
	2) id_Promocion
	Con estos datos voy a crear el registro en la tabla cupon y porteriormente
	le voy a regresar al usuario
	1) El descuento que puede obtener de esta promocion especificando si es el
		descuento debido o si es un desceunto menor debido a que los descuentos
		de su categoria (tipo de usuario) ya se terminaron.
	2) Todos los datos de la promocion.
	3) Todos los datos de la empresa.
"""
###{'pre':{'i':05,'a':05},'pla':{'i':05,'a':05},'gol':{'i':05,'a':05},'pmi':{'i':05,'a':05}}
###'{"pre": {"i": 5, "a": 0}, "gol": {"i": 5, "a": 0}, "pmi": {"i": 5, "a": 0}, "pla": {"i": 5, "a": 0}}'
###'{"pre": {"i": 5, "a": 0}, "gol": {"i": 5, "a": 0}, "pmi": {"i": 5, "a": 0}, "pla": {"i": 5, "a": 0}}'
def verificaDescuentoReal(miDescuentoEsDe = None,tarjetasDescuento = None):
	miDescuentoFinalEsDe = None 
	if miDescuentoEsDe.has_key("pre"):
		if tarjetasDescuento['pre']['i'] > tarjetasDescuento['pre']['a']:
			miDescuentoFinalEsDe = miDescuentoEsDe
	elif miDescuentoEsDe.has_key("pla"):
		if tarjetasDescuento['pla']['i'] > tarjetasDescuento['pla']['a']:
			miDescuentoFinalEsDe = miDescuentoEsDe
		else:
			des = miDescuentoEsDe['pla']
			verificaDescuentoReal({'pre':des - aumentoDescuento},tarjetasDescuento)
	elif miDescuentoEsDe.has_key("gol"):
		if tarjetasDescuento['gol']['i'] > tarjetasDescuento['gol']['a']:
			miDescuentoFinalEsDe = miDescuentoEsDe
		else:
			des = miDescuentoEsDe['gol']
			verificaDescuentoReal({'pla':des - aumentoDescuento},tarjetasDescuento)
	elif miDescuentoEsDe.has_key("pmi"):
		if tarjetasDescuento['pmi']['i'] > tarjetasDescuento['pmi']['a']:
			miDescuentoFinalEsDe = miDescuentoEsDe
		else:
			des = miDescuentoEsDe['pmi']
			verificaDescuentoReal({'gol':des - aumentoDescuento},tarjetasDescuento)
	return miDescuentoFinalEsDe

'{"pre": {"i": 5, "a": 0}, "gol": {"i": 5, "a": 0}, "pmi": {"i": 5, "a": 0}, "pla": {"i": 5, "a": 0}}'

def infoPromocionUser(id_user = None,id_promo = None,guardar=None,descuentoUs=None):
	if id_user and id_promo:
		try:
			promocion = Promocion.objects.get(pk=id_promo)
			
			empresa = promocion.empresa
			descuentoInicial = promocion.descuento
			costoPromocion = promocion.precio_total
			tarjetasDescuento = json.loads(promocion.tiposDescuentos)
			print "lo que obtengo es %s" % tarjetasDescuento
			if guardar is None:
				user = User.objects.get(pk=id_user)
				miDescuentoEsDe = obtenerMiDescuento(
									empresa,
									user,
									descuentoInicial)
		except Exception, e:
			raise
		if guardar and descuentoUs:
			datosGuardados = False
			descuentoFinal = verificaDescuentoReal(
								descuentoUs,  ##Verificar si es que no genera error por que no lo leo como json
								tarjetasDescuento)
			if descuentoFinal:
				folioCupon = "HTKFI48S" ### Invocar a funcion de saul para que me de el folio del cupon
				### Verifico si su funcion me regreso algo
				if folioCupon == "HTKFI48S":  
					try:
						cupon = Cupon(promocion = promocion,
									num_folio = folioCupon,
									usuario = id_user,
									tipo_user_tarjeta = descuentoFinal
								)
						cupon.save()
						if descuentoFinal.has_key("pre"):
							tarjetasDescuento['pre']['a'] += 1
						elif descuentoFinal.has_key("pla"):
							tarjetasDescuento['pla']['a'] += 1
						elif descuentoFinal.has_key("gol"):
							tarjetasDescuento['gol']['a'] += 1
						elif descuentoFinal.has_key("pmi"):
							tarjetasDescuento['pmi']['a'] += 1

						promocion.tiposDescuentos = json.dumps(tarjetasDescuento)
						promocion.save()
						datosGuardados = True
					except Exception, e:
						raise
			if datosGuardados:
				return True
			else:
				return False
		else:
			return {'promocion':promocion,
					'empresa':empresa,
					'miDescuentoEsDe':miDescuentoEsDe}
"""la siguiente funcion la voy a utilizar para cobrar la comisión
	que nos corresponde por la venta del cupon, voy a recibir como
	parametros 
	1) Cupon
	2) Empresa
	3) usuario
	4) Promocion

"""
def cobarComisionCupon(cupon= None,promocion=None,user = None):
	operacion = False

	costoPromo = promocion.precio_total
	empresa =  promocion.empresa
	capitalEmpresa = empresa.total_capital
	comisionPromo = redondeo(costoPromo * Decimal(porcentajeComision),2)
	print comisionPromo
	if capitalEmpresa > comisionPromo:
		empresa.total_capital -= comisionPromo
		empresa.save()
		###cupon.fecha_canjeado =  agregar la fecha de hoy
		###cupon.save()
		datos = {"transaccion":"efectiva",
				"nuevoCapitalEmpresa":str(empresa.total_capital)}
	else:
		datos = {"error":"CB-0005634",
				"capitalEmpresa":str(capitalEmpresa),
				"costoComision":str(comisionPromo)}
	return datos

	

def redondeo(cifra, digitos=2):
  """Rutina par redondeo de cifras decimales como para uso en contabilidad"""
  ### Symmetric Arithmetic Rounding for decimal numbers
  if type(cifra) != decimal.Decimal:
    cifra = decimal.Decimal(str(cifra))
  return cifra.quantize(decimal.Decimal("1") / (
  		decimal.Decimal('10') ** digitos), 
  		decimal.ROUND_HALF_UP)

def confirmarPagoPromocion(data= None,cobrarCom=False):
	data = json.loads(data)
	respuesta = {}
	correcto = False
	user = None 
	promo = None
	if data.has_key("tarjeta") and data.has_key("empresa"):
		if re.match("\w{3,10}",data["tarjeta"]) and re.match("\d{1,6}",str(data["empresa"])):
			try:
				usertarjeta = userTarjeta.objects.filter(
								tarjeta__dni=data["tarjeta"])[:1]
				for x in usertarjeta:
					if x.estado == "1":
						user = x.user
					else:
						respuesta["error"] = {"codigo":"CB-0005636",
											"estadoTarjeta":usertarjeta.estado}
			except Exception, e:
				raise

			if user:
				userMandar = {"nombre":user.first_name,
								"apellido":user.last_name}
				try:
					cupon = Cupon.objects.filter(
						usuario=user,
						promocion__empresa=data["empresa"],
						fecha_canjeado__isnull=True)[:1]

					if cupon:
						for aux in cupon:
							promo = aux.promocion

							promoMandar = retornaDatosParaMandar(promo)
						correcto = True
					else: 
						respuesta["error"] = {"codigo":"CB-0005635"}
				except Exception, e:
					raise
				if cobrarCom and correcto:
					respuesta = cobarComisionCupon(cupon,promo,user)
					print respuesta

				else:
					if correcto:
						respuesta = {"cupon":serializers.serialize('json', cupon),
									"promocion":json.dumps(promoMandar),
									"user":json.dumps(userMandar)}
			else:
				mesaje = json.dumps({"Error":"FOLIO-34X5-23",
					"Descripción": "Ocurrio un erro al realizar las consultas"})

		else:
			respuesta["error"] =  {"codigo":"CB-0005638",
									"empresa":data["empresa"],
									"tarjeta":data["tarjeta"]}

	elif data.has_key("cupon") and data.has_key("empresa"):		
		if re.match("\w{3,10}",data["cupon"]) and re.match("\d{1,6}",str(data["empresa"])):						
			try:
				cupon = Cupon.objects.filter(num_folio=data["cupon"])[:1]
				if cupon:
					for aux in cupon:
						promo = aux.promocion
						user = aux.usuario
						userMandar = {"nombre":user.first_name,
									"apellido":user.last_name}
						promoMandar = retornaDatosParaMandar(promo)
					respuesta = {"cupon":serializers.serialize('json', cupon),
									"promocion":json.dumps(promoMandar),
									"user":json.dumps(userMandar)}
					if cobrarCom and promo:
						respuesta = cobarComisionCupon(cupon,promo,user)
				else:
					respuesta["error"] = {"codigo":"CB-0005635"}
			except Exception, e:
				raise
		else:
			respuesta["error"] =  {"codigo":"CB-0005638",
									"empresa":data["empresa"],
									"cupon":data["cupon"]}

			
	else:
		respuesta["error"] =  {"codigo":"CB-0005637"}

	return json.dumps(respuesta)


def retornaDatosParaMandar(promo = None):
	if promo:
		return {"tipo_promocion":promo.tipo_promocion,
				"des_tipoPromo":promo.des_tipoPromo,
				"titulo_promocion":promo.titulo_promocion,
				"descripcion":promo.descripcion,
				"precio_total":str(promo.precio_total)}


			






