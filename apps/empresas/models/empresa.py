# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _
#from django_localflavor_mx.models import MXStateField, MXZipCodeField, 
# MXCURPField

choices_giro = [('ali','Alimentos'),('dep','Deportes'),('sal','Salud')]

choices_estados = (
	('AGU', 'Aguascalientes'),
	('BCN', 'Baja California'),
	('BCS', 'Baja California Sur'),
	('CAM', 'Campeche'),
	('CHH', 'Chihuahua'),
	('CHP', 'Chiapas'),
	('COA', 'Coahuila'),
	('COL', 'Colima'),
	('DIF', 'Distrito Federal'),
	('DUR', 'Durango'),
	('GRO', 'Guerrero'),
	('GUA', 'Guanajuato'),
	('HID', 'Hidalgo'),
	('JAL', 'Jalisco'),
	('MEX', 'Estado de México'),
	('MIC', 'Michoacán'),
	('MOR', 'Morelos'),
	('NAY', 'Nayarit'),
	('NLE', 'Nuevo León'),
	('OAX', 'Oaxaca'),
	('PUE', 'Puebla'),
	('QUE', 'Querétaro'),
	('ROO', 'Quintana Roo'),
	('SIN', 'Sinaloa'),
	('SLP', 'San Luis Potosí'),
	('SON', 'Sonora'),
	('TAB', 'Tabasco'),
	('TAM', 'Tamaulipas'),
	('TLA', 'Tlaxcala'),
	('VER', 'Veracruz'),
	('YUC', 'Yucatán'),
	('ZAC', 'Zacatecas'))

class Municipio(models.Model):
	estado =models.CharField(max_length=3,choices=choices_estados,default='PUE',
			verbose_name=_('Estado'))
	nombre = models.CharField(max_length=60,verbose_name=_('Municipio'))
	class Meta:
		verbose_name = _('Municipio')
		verbose_name_plural = _('Municipios')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)
	

class Empresa(models.Model):

	nombre = models.CharField(unique=True, max_length=50, 
				verbose_name=_('Nombre de la empresa'))
	giro = models.CharField(max_length=3,choices=choices_giro,
			 	verbose_name=_('Giro de la empresa'))
	telefono = models.CharField(max_length=15, blank=True)
	email = models.EmailField(null=True, blank=True, 
				verbose_name=_('Correo electronico'))
	sitio_web = models.URLField(null=True,blank=True,
				verbose_name=_('Sitio web'))
	municipio = models.ForeignKey('Municipio')
	colonia = models.CharField(max_length=70, verbose_name=_('Colonia'))
	direccion  = models.CharField(max_length=90, verbose_name=_('Direccion'))
	num_exterior = models.CharField(max_length=8,
				verbose_name=_('Numero exterior'))
	num_interior = models.CharField(max_length=8,blank=True, 
					verbose_name=_('Numero interior'))
	encargado = models.ForeignKey(User)
	latitud_mapa = models.FloatField(null=True,blank=True)
	longitud_mapa = models.FloatField(null=True,blank=True)
	class Meta:
		app_label = 'empresas'
		verbose_name = _('Empresa')
		verbose_name_plural = _('Empresas')

	def __unicode__(self):
		return '%s' %(self.nombre)
	