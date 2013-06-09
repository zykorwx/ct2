# -*- coding: utf-8 *-*
from apps.promociones.models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



admin.site.register(Categoria)
admin.site.register(Sub_categoria)
admin.site.register(Promocion)
admin.site.register(Especificaciones_promocion)





