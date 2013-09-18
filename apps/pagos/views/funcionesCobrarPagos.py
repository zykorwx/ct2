""" 
	Importando los modelos a utilizar 
	from django.contrib.auth.models import User
	from apps.promociones.models.promocion import Promocion
	from apps.cupones.models.cupon import Cupon
"""
"""
from apps.pagos.modeles import cobroCuponComision
from apps.empresas.models.empresa import Empresa
from apps.promociones.views.porcentajeComisionPromo import porcentajeComision
from apps.usuarios.models.MisCompras import ComprasEmpresaFavorita



def contarComprasEmpresasMatriz(empresas = None,user=None):
	compras = None
	if empresas:
		compras = ComprasEmpresaFavorita.objects.filter(
					empresa__in=empresas,us=user).aggregate(
					total=Sum('cantidad'))
	return compras

def obtenerComprasMatriz(matriz = None,user=None,descuentoInicial = 5):
	if matriz:
		descueto = descuentoInicial
		membresia = 'pre'
		empresas = Empresa.objects.filter(matriz=matriz)
		mis_compras = contarComprasEmpresasMatriz(empresas,user)
		if mis_compras:
			if mis_compras['total'] < 6:
				descuento = descuento
			elif mis_compras['total'] < 11:
				membresia = 'pla'
				descueto += 5
			elif mis_compras['total'] < 16:
				membresia = 'gol'
				descuento += 10
			else:
				membresia = 'pmi'
				descuento += 15
		return (membresia,descuento)
	else:
	 	return (None,None)

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





