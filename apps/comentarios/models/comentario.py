# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.promociones.models.promocion import Promocion


from django.utils.translation import ugettext_lazy as _



class Comentario_promocion(models.Model):
	promocion = models.ForeignKey(Promocion)
	comentarios = models.TextField(verbose_name=_('Comentario'), blank=True, null=True)

	class Meta:
		verbose_name = _('Comentario de la promocion')
		verbose_name_plural = _('Comentarios de las promociones')
		app_label='comentarios'
	def __unicode__(self):
		return '%s' %(self.comentarios)
	