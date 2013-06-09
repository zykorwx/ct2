# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.promociones.models.promocion import Promocion
from django.contrib.auth.models import User


from django.utils.translation import ugettext_lazy as _



class Comentario_promocion(models.Model):
	usuario = models.ForeignKey(User)
	promocion = models.ForeignKey(Promocion)
	comentario = models.TextField(verbose_name=_('Comentario'))
	fecha = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = _('Comentario de la promocion')
		verbose_name_plural = _('Comentarios de las promociones')
		app_label='comentarios'
	def __unicode__(self):
		return '%s' %(self.comentario)


class Calificacion_comentario(models.Model):
	comentario = models.ForeignKey(Comentario_promocion)
	usuario = models.ForeignKey(User)
	calificacion =  models.PositiveSmallIntegerField(
						verbose_name=(u'Calificacion'))

	class Meta:
		verbose_name = _('Calificar comentario')
		verbose_name_plural = _('Ingresar calificacion de comentarios')
		app_label= 'comentarios'
	def __unicode__(self):
		return '%s' %(self.calificacion)
	