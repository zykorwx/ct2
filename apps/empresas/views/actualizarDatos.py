#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect

from json import dumps, loads, JSONEncoder

from django.core.serializers import serialize
from django.core import serializers

from django.db.models.query import QuerySet
from django.utils.functional import curry



### Modelos
from apps.empresas.models import Empresa
from apps.empresas.models.BDlocalidades import Municipios,Localidades

### Formularios
from apps.empresas.forms.datosGeneralesForm import DatosGeneralesEmpresaForm


def selectMunicipios(request, id_estado):
	
	if request.is_ajax():
		mun = Municipios.objects.filter(estado=id_estado).order_by('nombre')
		###mun1 = Municipios.objects.filter(estado=id_estado).values('id', 'nombre')[0:10]
		###myModel.objects.filter(foo_icontains=bar).values('f1', 'f2', 'f3')
		if isinstance(mun, QuerySet):
			###print loads(serialize('json', mun))
			data = serializers.serialize('json', mun, fields=('id','nombre'))
			##print data
			return  HttpResponse(data)
	else:
		print "No fue en ujax"
		return HttpResponse('Lo sentimos No es una petición ajax')


def selectLocalidades(request, id_municipio):
	
	if request.is_ajax():
		###print "Yo ha anetradp"
		localidades = Localidades.objects.filter(municipio=id_municipio).order_by('nombre')
		###mun1 = Municipios.objects.filter(estado=id_estado).values('id', 'nombre')[0:10]
		###myModel.objects.filter(foo_icontains=bar).values('f1', 'f2', 'f3')
		if isinstance(localidades, QuerySet):
			###print loads(serialize('json', localidades))
			data = serializers.serialize('json', localidades, fields=('id','nombre'))
			###print data
			return  HttpResponse(data)
	else:
		print "No fue en ujax"
		return HttpResponse('Lo sentimos No es una petición ajax')

