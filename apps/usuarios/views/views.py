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


# Este index es solo para mostrar las opciones de login de la aplicacion
def  index(request):
	if request.user.is_authenticated():
		return redirect('/usuario/logeado')
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



# Este metodo solo una prueba para mostrar al usuario conectado y descargar su imagen de twitter
@login_required(login_url='/usuario')
def  logeado(request):
	# Las 3 siguientes lineas son importantes por que sin ellas no se mostraria la imagen de twitter
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
		return render_to_response('usuarios/logeado.html', {'imagenTwitter': getImgTwitter, 'nameTwitter': getNameTwitter, 'idTwitter':getIdTwitter, 'infoFacebook': getInfoFaceBook }, context_instance=RequestContext(request))
	return render_to_response('usuarios/logeado.html',  context_instance=RequestContext(request))


# Cerrar sesion abierta (cualquiera)
@login_required(login_url='/usuario')
def cerrarSesion(request):
	logout(request)
	return HttpResponseRedirect('/usuario')

# Logeo por medio de email de cualquier tipo de usuario (Empresas, Consumidores que no se hayan registrado usando redes sociales)
def login(request):
	if request.user.is_authenticated():
		return redirect('/usuario')
	else:
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/usuario')
			else:
				return render_to_response('usuarios/login.html', \
					context_instance=RequestContext(request))
		else:
			return render_to_response('usuarios/login.html', \
				context_instance=RequestContext(request))
