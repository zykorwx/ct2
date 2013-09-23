#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect
from django.contrib.auth.models import User
from apps.usuarios.forms import RegistroEmpresaForm
from apps.empresas.models import Empresa
from django.core.mail import EmailMultiAlternatives
from django.db import DatabaseError, IntegrityError
# Este es un helper creado en la vista de esta aplicacion
from views import verficaGrupo
import random
import string


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
				enviaCorreoConfirmacion(perfil_empresa)
				return HttpResponseRedirect('/')
		else:
			mensaje ="Los datos no son validos"
			formulario =RegistroEmpresaForm()
		return render_to_response('usuarios/registro.html',{'formulario': formulario, 'tipo':'Empresa'  }, \
				context_instance=RequestContext(request))


def enviaCorreoConfirmacion(empresa):
	if (empresa.codigo_confirmacion == None or empresa.codigo_confirmacion == ""):
		codigo = ''.join(random.choice(string.letters) for i in xrange(32))
		empresa.codigo_confirmacion = codigo
	else: 
		codigo = empresa.codigo_confirmacion
	empresa.is_active = False
	empresa.save()
	titulo = 'Correo de confirmación Filper'
	url = reverse('user_confirm', kwargs={'empresa_id': empresa.id, 'codigo': codigo})
	texto_contenido = u'Has clic en el siguiente enlace para confirmar tu correo electrónico. <a href="http://localhost:8000/%s"> Confirmar</a>' % url
	html_contenido = u'<h1>%s</h1><p>Has clic en el siguiente enlace para confirmar tu correo electrónico.</p> <a href="http://localhost:8000%s"> Confirmar</a>' % (empresa.nombre, url)
	msg = EmailMultiAlternatives(titulo, texto_contenido, 'contacto@filper.com', [empresa.email])
	msg.attach_alternative(html_contenido, "text/html")
	msg.send()



def reenviaCorreoConfirmacion(request, empresa_id):
	if request.user.is_authenticated():
		try:
			empresa = Empresa.objects.get(pk=empresa_id)
			enviaCorreoConfirmacion(empresa)
			return redirect('/empresa')
		except DatabaseError as e:
			return HttpResponse(json.dumps({"error": "database error"}), content_type="application/json")					
		except IntegrityError as e:
			return HttpResponse(json.dumps({"error": "integridad"}), content_type="application/json")	
		except Comentario_promocion.DoesNotExist:
			return HttpResponse(json.dumps({"error": "Sin resultados"}), content_type="application/json")	
	else:
		return redirect('/')


def confirm(request, empresa_id, codigo):
    try:
        empresa = Empresa.objects.get(pk=empresa_id, codigo_confirmacion=codigo)
    except Empresa.DoesNotExist:
        # wrong key, do something, redirect to somewhere etc
        template = '/'
    else:
        empresa.is_active = True
        empresa.save()
        template = '/empresa'
    return HttpResponseRedirect(template)

