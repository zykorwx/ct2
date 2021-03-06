#encoding:utf-8
# Este archivo lo ocupo como un helper y pongo metodos pequeños
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext #se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las funciones
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.db import DatabaseError, IntegrityError
from apps.usuarios.models import Perfil
from social_auth.models import UserSocialAuth
from apps.empresas.models import Empresa, Encargados_empresas,Categoria
from apps.usuarios.decorators import login_empresa_required
import json

### Formulario para actualizar los datos
from apps.empresas.forms.datosGeneralesForm import DatosGeneralesEmpresaForm

### Api de Google Places.
from googleplaces import GooglePlaces, types, lang
PLACES_API_KEY = 'AIzaSyCy1NFjXXz9R2VV9vaZ0VQVKolvKyazR8k' ### Mi clave de de consola Google
google_places = GooglePlaces(PLACES_API_KEY)



### Modelos que utilizo (Froy)
from apps.empresas.models.BDlocalidades import Localidades


# Este index es solo para mostrar las opciones de login de la aplicacion
def  index(request):
	if request.user.is_authenticated():
		if request.user.social_auth.filter().count() > 0:
			verficaGrupo(request.user, 'consumidor')
			verificaPerfil(request.user)
			if request.user.social_auth.filter(provider='twitter').count() > 0:
				getImgTwitter = request.user.social_auth.get(provider='twitter').extra_data['profile_image_url']
				getNameTwitter = request.user.social_auth.get(provider='twitter').extra_data['screen_name']
				getIdTwitter = request.user.social_auth.get(provider='twitter').id
				getImgTwitter = getImgTwitter.replace('_normal', '_bigger')
			else:
				getImgTwitter = ''
				getNameTwitter = ''
				getIdTwitter = ''
			if request.user.social_auth.filter(provider='facebook').count() > 0:
				getInfoFaceBook = 'https://graph.facebook.com/%s?fields=first_name,picture.type(large)' % request.user.social_auth.get(provider='facebook').uid
			else:
				getInfoFaceBook = ''
			# Las siguientes lineas validan si el usuario que se logea es encargado de alguna empresa
			# y retorna las empresas que administra
			encargado = Encargados_empresas.objects.filter(user = request.user)
			return render_to_response('usuarios/index.html', {'imagenTwitter': getImgTwitter,
			 'nameTwitter': getNameTwitter,
			 'idTwitter':getIdTwitter,
			 'infoFacebook': getInfoFaceBook,
			 'encargado': encargado},
			 context_instance=RequestContext(request))
		if request.user.groups.filter(id=1).count() > 0:
			return render_to_response('usuarios/index.html',  context_instance=RequestContext(request))
		return HttpResponseRedirect('/empresa')
	else:
		return render_to_response('usuarios/index.html',  context_instance=RequestContext(request))


# Si no existe el grupo lo creamos y agregamos al usuario, si existe solo agregamos al usuario
def verficaGrupo(usuario, nombre):
	aux = Group.objects.filter(name=nombre)
	if aux.count() == 0:
		grupo = Group(name=nombre)
		grupo.save()
		usuario.groups.add(grupo)
	else:
		usuario.groups.add(aux[0])


# Verificamos si ya se creo el perfil del usuario de los datos de facebook
# Si es que no, obtenemos los datos desde el json de social auth y los metemos al perfil
# Si ya existe pero los datos no son iguales a los que tenemos en el social auth los actualizamos
# Esto quiere decir si el usuario cambia algo en el facebook tambien lo cambiara en su perfil de nuestra pagina
def verificaPerfil(usuario):
	try:
		perfil = Perfil.objects.get(pk=usuario)
		datosFace = usuario.social_auth.get(provider='facebook').extra_data
		if str(perfil.json_facebook) != str(datosFace):
			return guardaPerfil(usuario)
		return True
	except DatabaseError as e:
		return False					
	except IntegrityError as e:
		return False	
	except Perfil.DoesNotExist:
		return guardaPerfil(usuario) 

# guarda el perfil de usuario
def guardaPerfil(usuario):
	try:
		datosFace = usuario.social_auth.get(provider='facebook').extra_data
		if (datosFace['birthday'] != None) and (datosFace['gender'] != None) and (datosFace['hometown'] != None) and (datosFace['id'] != None):
			perfil = Perfil(usuario.id, datosFace['birthday'], datosFace['gender'], datosFace['hometown']['name'], datosFace['id'], datosFace)
			perfil.save()
			return True
	except DatabaseError as e:
		return False					
	except IntegrityError as e:
		return False
	except usuario.social_auth.DoesNotExist:
		return False


### Se debe verificar el seguimiento, pero eso ya cuando se vaya creadno el
### sistema final.
@login_empresa_required(login_url='/')
def logeoEmpresa(request):
	print "llego aqui?"
	verificado = False
	empresa = Empresa.objects.filter(empresa_user = request.user.id)
	item_empresa = get_object_or_404(Empresa, pk=1)
	dominio = 'http://www.' + empresa[0].email.split("@")[-1] # Obtenemos el dominio del correo de la empresa
	encargados = Encargados_empresas.objects.filter(empresa = empresa[0].id)
	### Verifico si es un un formulario valido para actualizar los datos.
	if request.method == "POST":
		form = DatosGeneralesEmpresaForm(request.POST)
		if form.is_valid():
			local_empresa = Localidades.objects.get(pk=form.cleaned_data['localidad'])
			giro_empresa = Categoria.objects.get(pk=form.cleaned_data['giro']) 
			item_empresa.localidad = local_empresa
			item_empresa.giro = giro_empresa
			item_empresa.telefono = form.cleaned_data['telefono']
			item_empresa.sitio_web = form.cleaned_data['sitio_web']
			item_empresa.direccion = form.cleaned_data['direccion']
			item_empresa.LatLng = form.cleaned_data['Latlng']

			lt = form.cleaned_data['Latlng'][1:-1]
			l= lt.split(',')
			aux = add_google_place("Viewor",{'lat':float(l[0]),'lng':float(l[1])}, "book_store")
			item_empresa.id_place = aux['id']
			item_empresa.reference_place = aux['reference']
			item_empresa.save()
			

			###print empresa
			###add_google_place("Viewor",{'lat':float(l[0]),'lng':float(l[1])}, "book_store")
			return render_to_response('usuarios/empresa_logeado.html', 
				{'empresa': empresa[0], 'encargados': encargados, 'dominio': dominio},
				 context_instance=RequestContext(request))
	form_actualiza = DatosGeneralesEmpresaForm()
	return render_to_response('usuarios/empresa_logeado.html', 
		{'empresa': empresa[0], 'encargados': encargados, 'dominio': dominio,
		'form_actualiza': form_actualiza},
		 context_instance=RequestContext(request))


# Cerrar sesion abierta (cualquiera)
@login_required(login_url='/')
def cerrarSesion(request):
	logout(request)
	return HttpResponseRedirect('/')

# Logeo por medio de email de cualquier tipo de usuario (Empresas, Consumidores que no se hayan registrado usando redes sociales)
def login(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/')
			else:
				return render_to_response('usuarios/login.html', \
					context_instance=RequestContext(request))
		else:
			return render_to_response('usuarios/login.html', \
				context_instance=RequestContext(request))

def vinculaCuentaXFacebook(request, facebook_uid):
	userFacebook = UserSocialAuth.objects.filter(uid=facebook_uid)
	if userFacebook.count() > 0:
		user = User.objects.get(pk = userFacebook[0].user_id )
		empresa = Empresa.objects.filter(empresa_user = request.user)
		if empresa.count() > 0: # Dejo esta validacion en caso de en un futuro ingresar sucursales
			vincular = Encargados_empresas.objects.get_or_create(user = user, empresa = empresa[0])
			logout(request)
			# El proposito de la siguiente linea es solo mostrar que el usuario que ha sido vinculado, no es esencial
			# y debe ser cambiado este comportamiento, dado que no regresa una lista de usuarios vinculados
			return redirect('/login/facebook/')
	else:
		empresa = Empresa.objects.filter(empresa_user = request.user)
		if empresa.count() > 0: # Dejo esta validacion en caso de en un futuro ingresar sucursales
			# Cerramos sesion de la empresa y logeamos al nuevo usuario, y despues lo vinculamos a la empresa
			logout(request)
			# Despues de logearse el usuario, se envia a la siguiente ruta donde se vincula por medio del id
			# de la empresa
			return redirect('/login/facebook/?next=/vinculaCuentaXEmpresa/%s' % empresa[0].id)
		

def vinculaCuentaXEmpresa(request, empresa_id):
	# Resive el id de la empresa con el que se obtine el objeto y y solo con el request del user 
	# vinculamos las cuentas
	empresa = Empresa.objects.get(pk = empresa_id)
	vincular = Encargados_empresas.objects.get_or_create(user = request.user, empresa = empresa)
	return redirect('/')




def add_google_place(nombre_local="", latlon="", type_place=""):
	print nombre_local
	print latlon
	try:
		print nombre_local
		print latlon
		added_place = google_places.add_place(name=nombre_local,
				lat_lng=latlon,
				accuracy=50,
				types=types.TYPE_HOME_GOODS_STORE,
				language=lang.SPANISH)
		print added_place # The Google Places reference - Important!
		return added_place
	except:
		# You've passed in parameter values that the Places API doesn't like..
		print "error_detail"


