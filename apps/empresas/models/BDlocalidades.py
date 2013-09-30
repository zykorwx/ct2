#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Estados(models.Model):
	clave =models.CharField(max_length=2,verbose_name=_('Clave'))
	nombre = models.CharField(max_length=45,verbose_name=_('Estado'))
	abrev = models.CharField(max_length=16,verbose_name=_('Abreviatura'))
	class Meta:
		verbose_name = _('Estado')
		verbose_name_plural = _('Estados')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)



class Municipios(models.Model):
	estado = models.ForeignKey(Estados)
	clave =models.CharField(max_length=3,verbose_name=_('Clave'))
	nombre = models.CharField(max_length=50,verbose_name=_('Nombre'))
	sigla = models.CharField(max_length=4,verbose_name=_('Sigla'))

	class Meta:
		verbose_name = _('Municipio')
		verbose_name_plural = _('Municipios')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)



class Localidades(models.Model):
	municipio = models.ForeignKey(Municipios)
	clave =models.CharField(max_length=4,verbose_name=_('Clave'))
	nombre = models.CharField(max_length=110,verbose_name=_('Nombre'))
	latitud = models.CharField(max_length=6,verbose_name=_('Latitud'))
	longitud = models.CharField(max_length=7,verbose_name=_('Longitud'))
	altitud = models.CharField(max_length=4,verbose_name=_('Altitud'))
	class Meta:
		verbose_name = _('Localidad')
		verbose_name_plural = _('Localidades')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)


