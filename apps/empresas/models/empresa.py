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
	fecha_alta = models.DateTimeField(auto_now=True,default='2013-07-07 17:27:17')
	latitud_mapa = models.FloatField(null=True,blank=True)
	longitud_mapa = models.FloatField(null=True,blank=True)
	is_active = models.BooleanField(default=True) 
	class Meta:
		app_label = 'empresas'
		verbose_name = _('Empresa')
		verbose_name_plural = _('Empresas')

	def __unicode__(self):
		return '%s' %(self.nombre)


CONCEPTOS = (
	('1', _('Inscripcion')),
	('0', _('Mensualidad')),
)
FORMASPAGO = (
	('1', _('Contado')),
	('0', _('Credito')),
)

class pagoEmpresa(models.Model):
	empresa = models.ForeignKey(Empresa)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2,default=0.0,
									verbose_name=_(u'Monto a pagar $'))
	fecha_pago = models.DateTimeField(auto_now=True)
	concepto = models.CharField(max_length=1, choices=CONCEPTOS, 
								verbose_name=_('Concepto de pago'), default='1')
	formaPago = models.CharField(max_length=1, choices=FORMASPAGO, 
								verbose_name=_('Forma de pago'), default='0')

	def __unicode__(self):
		return u'Empresa: %s - Fecha de pago: %s' % (self.empresa, 
														self.fecha_pago)

	class Meta:
		app_label = 'empresa'
