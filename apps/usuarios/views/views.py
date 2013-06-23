#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext #se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las funciones
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Este index es solo para mostrar las opciones de login de la aplicacion
def  index(request):
	return render_to_response('usuarios/index.html',  context_instance=RequestContext(request))

# Este metodo solo una prueba para mostrar al usuario conectado y descargar su imagen de twitter
@login_required(login_url='/usuario')
def  logeado(request):
	# Las 3 siguientes lineas son importantes por que sin ellas no se mostraria la imagen de twitter
	if request.user.social_auth.filter(provider='twitter').count() > 0:
		getImg = request.user.social_auth.get(provider='twitter').extra_data['profile_image_url']
		return render_to_response('usuarios/logeado.html', {'imagen': getImg }, context_instance=RequestContext(request))
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
