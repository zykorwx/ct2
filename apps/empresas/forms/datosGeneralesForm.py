# -*- coding: utf-8 *-*
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

### Importando los modelos que voy a utilizar para hacer el formulario
from apps.empresas.models.BDlocalidades import *
from apps.empresas.models.empresa import Categoria

import re



# Creamos campo personalizado de RFC, comprobamos que no exista otro igual y lo validamos
class RFCField(forms.CharField):
    def clean(self, value):
        super(RFCField, self).clean(value)
        try:
            User.objects.get(username=value)
            raise forms.ValidationError("El RFC ya existe. Por favor verifique sus datos.")
        except User.DoesNotExist:
            if re.match("([A-Z]{4})(\d{6})(\w{3})", value.upper()) == None:
                raise forms.ValidationError("El RFC no es valido por favor verifique sus datos.")
            return value.upper()



# Fomr del registro de usuario en email asignamos nuestro campo personalizado
# Recordar first_name = Nombre de la empresa
# last_name = Nombre del encargado de la empresa
# Para cambiar el label mostrado solo cambiar la propiedar label de cada campo
class DatosGeneralesEmpresaForm(forms.Form):
    estado = forms.IntegerField(widget=forms.Select(choices=Estados.objects.all().values_list('id','nombre')))
    muicipio = forms.IntegerField(widget=forms.Select(choices=""))
    localidad = forms.IntegerField(widget=forms.Select(choices=""))
    giro = forms.CharField(widget=forms.Select(choices=Categoria.objects.all().values_list('id','nombre').order_by('nombre')))
    telefono = forms.CharField(max_length=15, label=_(u"Telefono"))
    direccion = forms.CharField(max_length=89, label=_(u"Direccion"))
    sitio_web = forms.URLField(label=_(u"Sitio web"))
    Latlng = forms.CharField(widget=forms.HiddenInput())

"""
    # Comprobamos contraseña
    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Las contraseñas no son iguales')
        return self.data['password']
    
    # comprobamos email y password
    def clean(self,*args, **kwargs):
        self.cleaned_data.get('email')
        self.clean_password()

"""