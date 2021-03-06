# -*- coding: utf-8 *-*
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
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
class RegistroEmpresaForm(forms.Form):
    first_name = forms.CharField(max_length=50, label=_(u"Nombre la empresa"))
    rfc = RFCField(max_length=15, label=_(u"R.F.C."))
    email = forms.EmailField(label=_(u"Correo electronico"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_(u"Contraseña"))
    password2 = forms.CharField(widget=forms.PasswordInput(), label=_(u"Repita contraseña"))


    # Comprobamos contraseña
    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Las contraseñas no son iguales')
        return self.data['password']
    
    # comprobamos email y password
    def clean(self,*args, **kwargs):
        self.cleaned_data.get('email')
        self.clean_password()
        return super(RegistroEmpresaForm, self).clean(*args, **kwargs)

