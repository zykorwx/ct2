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
	dni = models.CharField(max_length=20)
	tipo_tarjera = models.CharField(max_length=2,choices=tipo_tarjeta,
						default='pr')
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
	
	

User.add_to_class('id_tarjeta',models.ManyToManyField(Tarjeta,through=userTarjeta))



def get_image_path(perfil, filename):
    return os.path.join('imagenes/usuarios/usr_'+perfil.user.username, 'avatar',
    					 filename)


class Perfil(models.Model):
	user = models.ForeignKey(User, unique=True)
	avatar = models.ImageField(upload_to=get_image_path, verbose_name='avatar')
	tipo_user_tarjera = models.CharField(max_length=2,choices=tipo_tarjeta,
						default='pr')
	class Meta:
		verbose_name = _('Perfil')
		verbose_name_plural = _('Perfiles')
		app_label= 'usuarios'
	def __unicode__(self):
		return '%s' %(self.tipo_user_tarjera)
	



