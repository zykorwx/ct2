# -*- coding: utf-8 *-*
from apps.empresas.models import *
from apps.empresas.models.BDlocalidades import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin




admin.site.register(Localidades)
admin.site.register(Empresa)
admin.site.register(Categoria)

