# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.promociones.models.promocion import Promocion
from apps.usuarios.models.perfil import tipo_tarjeta
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Cupon(models.Model):
	promocion = models.ForeignKey(Promocion)
	num_folio = models.CharField(max_length=10, 
					verbose_name=_('Codigo unico de folio'))
	usuario = models.ForeignKey(User)
	canjeado = models.BooleanField(default=False) 
	fecha_solicitud = models.DateTimeField(auto_now=True)
	fecha_canjeado = models.DateField(blank=True, null=True)
	tipo_user_tarjeta = models.CharField(max_length=2,choices=tipo_tarjeta,
						default='pr')
	class Meta:
		verbose_name = _('Cupon')
		verbose_name_plural = _('Cupones')
		app_label= 'cupones'
	def __unicode__(self):
		pass
	