# -*- coding: utf-8 *-*


from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import os


tipo_tarjeta = [('pr','Preferente'),('pl','Platino'),
				('gl','Golden'),('pm','Premier')]

estado_tarjeta = [('1','Activa'),
				('2','Suspendida'),('3','Extraviada'),
				('4','Reportada como robada')]

tarjeta_es = [('1','Disponible'),
				('2','No Disponible')]


class Tarjeta(models.Model):
	dni = models.CharField(max_length=10)
	estado = models.CharField(max_length=1,choices=tarjeta_es)
	class Meta:
		verbose_name = _('Tarjeta')
		verbose_name_plural = _('Tarjetas')
		app_label= 'usuarios'
	def __unicode__(self):
		return '%s' %(self.dni)
	


class userTarjeta(models.Model):
	user = models.ForeignKey(User)
	tarjeta = models.ForeignKey('Tarjeta')
	fecha_alta = models.DateTimeField(auto_now=True)
	fecha_baja = models.DateTimeField(blank=True)
	estado = models.CharField(max_length=1,choices=estado_tarjeta)
	class Meta:
		app_label= 'usuarios'
	def __unicode__(self):
		return '%s' %(self.tarjeta)
	
	





def get_image_path(perfil, filename):
    return os.path.join('imagenes/usuarios/usr_'+perfil.user.username, 'avatar',
    					 filename)


class Perfil(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	fecha_nacimiento = models.CharField(max_length=15, verbose_name=(u'fecha_nacimiento'), blank=True, null=True)
	sexo = models.CharField(max_length=10, verbose_name=(u'Sexo'), blank=True, null=True)
	ubicacion = models.CharField(max_length=70, verbose_name=(u'Ubicacion'), blank=True, null=True)
	uid_facebook = models.CharField(max_length=20, verbose_name=(u'uid_facebook'), blank=True, null=True)
	json_facebook = models.TextField(blank=True, null=True, verbose_name=(u'Facebook'))
	class Meta:
		verbose_name = _('Perfil')
		verbose_name_plural = _('Perfiles')
		app_label= 'usuarios'
	def __unicode__(self):
		return '%s %s' %(self.user.first_name, self.user.last_name)




