from apps.usuarios.models.perfil import Perfil
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.register(Perfil)
