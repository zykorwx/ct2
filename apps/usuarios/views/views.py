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
from social_auth.models import UserSocialAuth
from apps.empresas.models import Empresa, Encargados_empresas
from apps.usuarios.decorators import login_empresa_required


# Este index es solo para mostrar las opciones de login de la aplicacion
def  index(request):
	if request.user.is_authenticated():
		if request.user.social_auth.filter().count() > 0:
			verficaGrupo(request.user, 'consumidor')
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


@login_empresa_required(login_url='/')
def logeoEmpresa(request):
	empresa = Empresa.objects.filter(empresa_user = request.user.id)
	dominio = 'http://www.' + empresa[0].email.split("@")[-1] # Obtenemos el dominio del correo de la empresa
	encargados = Encargados_empresas.objects.filter(empresa = empresa[0].id)
	return render_to_response('usuarios/empresa_logeado.html', {'empresa': empresa[0], 'encargados': encargados, 'dominio': dominio}, context_instance=RequestContext(request))


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




