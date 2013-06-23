#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect
from django.contrib.auth.models import User
from usuarios.forms import RegistroEmpresaForm


# Este es para registrar una nueva empresa
def nuevaEmpresaView(request):
	if request.user.is_authenticated() and not request.user.is_staff:
		return redirect('/')
	else:
		if request.method == 'POST':
			formulario = RegistroEmpresaForm(request.POST)
			if formulario.is_valid():
				password = formulario.cleaned_data['password']
				email = formulario.cleaned_data['email']
				new_user = User.objects.create_user(email, email, password)
				new_user.is_active=True
				new_user.is_staff=False
				new_user.is_superuser=False
				new_user.first_name=formulario.cleaned_data['first_name']
				new_user.last_name=formulario.cleaned_data['last_name']
				new_user.save()
				return HttpResponseRedirect('/usuarios')
		else:
			mensaje ="Los datos no son validos"
			formulario =RegistroEmpresaForm()
		return render_to_response('usuarios/registro.html',{'formulario': formulario, 'tipo':'Empresa'  }, \
				context_instance=RequestContext(request))
