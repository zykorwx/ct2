from apps.usuarios.models.MisCompras import ComprasPasadas

### esta funcion la utilizo unicamente para modificar el campo cantidad,
### por cada vez que el usuario compre un producto el campo se va a modificar
### en el caso de que noexita se vaa crear el objeto

def AgregarCompra(user= None, tag_compra=None):
	try:
		obj, creado = ComprasPasadas.objects.get_or_create(
						    us = user,
						    tag  = tag_compra,
						     defaults={'cantidad': 1}
						)
		if not creado:
			obj.cantidad += 1
			obj.save()
		return True
	except:
		return False


### Funcion para tener presente en que empresas es en las que más compra
### el usuario
def AgregarEmpresaFavorita(user= None, emp_fav=None):
	try:
		obj, creado = ComprasEmpresaFavorita.objects.get_or_create(
						    us = user,
						    empresa  = emp_fav,
						     defaults={'cantidad': 1}
						)
		if not creado:
			obj.cantidad += 1
			obj.save()
		return True
	except:
		return False
