# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.promociones.models.promocion import Promocion

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Cupon(models.Model):
	promocion = models.ForeignKey(Promocion)
	num_folio = models.CharField(max_length=10, 
					verbose_name=_('Codigo unico de folio'))
	usuario = models.ForeignKey(User)
	fecha_solicitud = models.DateTimeField(auto_now_add=True)
	fecha_canjeado = models.DateField(blank=True, null=True)
	tipo_user_tarjeta = models.CharField(max_length=13)
	empleado_atend = models.CharField(max_length=10,blank=True)
	class Meta:
		verbose_name = _('Solicitar un Cupon')
		verbose_name_plural = _('Solicitar Cupones')
		app_label= 'cupones'
	def __unicode__(self):
		return '%s' %(self.num_folio)
