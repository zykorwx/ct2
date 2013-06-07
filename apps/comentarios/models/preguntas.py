# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.promociones.models.promocion import Promocion

from django.utils.translation import ugettext_lazy as _




class Preguntas_promocion(models.Model):
	#promocion = models.ForeignKey(Promocion)
	pregunta = models.CharField(max_length=45,verbose_name=(u'Pregunta'))
	class Meta:
		verbose_name = _('Preguntas_promocion')
		verbose_name_plural = _('Preguntas_promociones')
		app_label ='comentarios'
	def __unicode__(self):
		return '%s' &(self.pregunta)
	



class Calificacion_promocion(models.Model):
	promocion = models.ForeignKey(Promocion)
	pregunta = models.ForeignKey(Preguntas_promocion)
	usuario = models.ForeignKey(User)
	calificacion =  models.PositiveSmallIntegerField(
						verbose_name=(u'Calificacion'))
	class Meta:
		verbose_name = _('Calificacion_promocion')
		verbose_name_plural = _('Calificacion_promociones')
		app_label = 'comentarios'
	def __unicode__(self):
		pass
