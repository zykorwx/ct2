# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import os

tipo_tarjeta = [('pr','Preferente'),('pl','Platino'),
				('gl','Golden'),('pm','Premier')]


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
	