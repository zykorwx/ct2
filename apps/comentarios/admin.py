# -*- coding: utf-8 *-*
from apps.comentarios.models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin




admin.site.register(Comentario_promocion)

admin.site.register(Calificacion_comentario)

admin.site.register(Preguntas_promocion)

admin.site.register(Calificacion_promocion)

