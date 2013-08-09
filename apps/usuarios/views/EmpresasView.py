#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect
from django.contrib.auth.models import User
from apps.usuarios.forms import RegistroEmpresaForm
from apps.empresas.models import Empresa
# Este es un helper creado en la vista de esta aplicacion
from views import verficaGrupo


# Este es para registrar una nueva empresa
def nuevaEmpresaView(request):
	if request.user.is_authenticated() and not request.user.is_staff:
		return redirect('/')
	else:
		if request.method == 'POST':
			formulario = RegistroEmpresaForm(request.POST)
			if formulario.is_valid():
				# Leemos los datos desde el formulario
				nombre = formulario.cleaned_data['first_name']
				password = formulario.cleaned_data['password']
				email = formulario.cleaned_data['email']
				rfc = formulario.cleaned_data['rfc']
				# Creamos el nuevo usuario
				new_user = User.objects.create_user(rfc, email, password)
				new_user.is_active=True
				new_user.is_staff=False
				new_user.is_superuser=False
				new_user.first_name=formulario.cleaned_data['first_name']
				new_user.save()
				# Agregamos al usuario al grupo empresa
				verficaGrupo(new_user, 'empresa')
				# Creamos el perfil de la empresa
				perfil_empresa = Empresa.objects.create(nombre = nombre, email = email, rfc = rfc, empresa_user = new_user)
				return HttpResponseRedirect('/usuario')
		else:
			mensaje ="Los datos no son validos"
			formulario =RegistroEmpresaForm()
		return render_to_response('usuarios/registro.html',{'formulario': formulario, 'tipo':'Empresa'  }, \
				context_instance=RequestContext(request))