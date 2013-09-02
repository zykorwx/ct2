# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models.empresa import Empresa, Tags
from django.utils.translation import ugettext_lazy as _


class ComprasPasadas(models.Model):
	us = models.ForeignKey(User)
	tag = models.ForeignKey(Tags)
	cantidad = models.PositiveSmallIntegerField()

	class Meta:
		app_label = 'usuarios'
		verbose_name = _('Mis_Compras_user')
		verbose_name_plural = _('Mis_Compras')
	def __unicode__(self):
		return '%s' %(self.cantidad)



class ComprasEmpresaFavorita(models.Model):
	us = models.ForeignKey(User)
	empresa = models.ForeignKey(Empresa)
	cantidad = models.PositiveSmallIntegerField()

	class Meta:
		app_label = 'usuarios'
		verbose_name = _('Mis_Compras_user_Empresa')
		verbose_name_plural = _('Mis_Compras_Empresa')
	def __unicode__(self):
		return '%s' %(self.cantidad)




