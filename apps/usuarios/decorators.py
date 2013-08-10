# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
# Decorador para verificar si el usuario conectado
# Es una empresa
# la segunda linea no recuerdo que hace pero la dejare asi por si acaso

class login_empresa_required(object):
    "Un decorador amb fam"
    def __init__(self, login_url='/'):
        self.login_url = login_url

    def __call__(self, f):
        def is_login(request, *args, **kw_args):
        	if not request.user.groups.filter(name = 'empresa').exists():
        		return HttpResponseRedirect(self.login_url)
        	else:
        		return f(request, *args, **kw_args)
        is_login.__name__ = f.__name__
        is_login.__doc__ = f.__doc__
        return is_login