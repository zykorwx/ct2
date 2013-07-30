# -*- coding: utf-8 *-*
from apps.empresas.models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin




admin.site.register(Municipio)
admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Sub_categoria)
