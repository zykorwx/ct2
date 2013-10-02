#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect
from django.db import DatabaseError, IntegrityError
from django.core import serializers
import json



def indexInvitaciones(request):
	if request.user.is_authenticated():
		return render_to_response('pruebas/angular.html', context_instance=RequestContext(request))
	else:
		return redirect('/')
