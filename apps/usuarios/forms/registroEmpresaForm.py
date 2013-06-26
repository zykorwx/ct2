# -*- coding: utf-8 *-*
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Creamos campo personalizado de username, y comprobamos que no exista otro igual
class UserField(forms.EmailField):
    def clean(self, value):
        super(UserField, self).clean(value)
        try:
            User.objects.get(username=value)
            raise forms.ValidationError("El nombre de usuario ya existe. Por favor elija otro.")
        except User.DoesNotExist:
            return value

# Fomr del registro de usuario en email asignamos nuestro campo personalizado
# Recordar first_name = Nombre de la empresa
# last_name = Nombre del encargado de la empresa
# Para cambiar el label mostrado solo cambiar la propiedar label de cada campo
class RegistroEmpresaForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_(u"Nombre la empresa"))
    last_name = forms.CharField(max_length=70, label=_(u"Nombre completo del encargado"))
    email = UserField(label=_(u"Email"))
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

