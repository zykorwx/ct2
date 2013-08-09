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
	
### Falta agregar el campo para logo de la empresa 
class Empresa(models.Model):
	empresa_user = models.ForeignKey(User)
	nombre = models.CharField(unique=True, max_length=50, 
				verbose_name=_('Nombre de la empresa'))
	giro = models.ForeignKey('Categoria', null=True)
	telefono = models.CharField(max_length=15, blank=True)
	rfc = models.CharField(max_length=15, unique=True)
	email = models.EmailField(null=True, blank=True, 
				verbose_name=_('Correo electronico'))
	sitio_web = models.URLField(null=True,blank=True,
				verbose_name=_('Sitio web'))
	municipio = models.ForeignKey('Municipio', null=True)
	colonia = models.CharField(blank=True, max_length=70, verbose_name=_('Colonia'))
	direccion  = models.CharField(max_length=90, verbose_name=_('Direccion'))
	num_exterior = models.CharField(blank=True, max_length=8,
				verbose_name=_('Numero exterior'))
	num_interior = models.CharField(max_length=8,blank=True, 
					verbose_name=_('Numero interior'))
	fecha_alta = models.DateTimeField(auto_now=True)
	latitud_mapa = models.FloatField(null=True,blank=True)
	longitud_mapa = models.FloatField(null=True,blank=True)
	is_active = models.BooleanField(default=True) 
	total_capital =  models.DecimalField(max_digits=7, decimal_places=2,
											default=0.0)
	class Meta:
		app_label = 'empresas'
		verbose_name = _('Empresa')
		verbose_name_plural = _('Empresas')

	def __unicode__(self):
		return '%s' %(self.nombre)

# Se crea esta tabla para vincular los encargados que pueda tener una empresa
class Encargados_empresas(models.Model):
	user = models.ForeignKey(User)
	empresa = models.ForeignKey(Empresa)

	class Meta:
		app_label = 'empresas'
		verbose_name = _('Encargado_empresa')
		verbose_name_plural = _('Encargados_empresas')


#Modelo para crear las categorias a las que van a pertenecer las proociones
class Categoria(models.Model):
	nombre =models.CharField(max_length=30, verbose_name=_('Categoria'))
	class Meta:
		verbose_name = _('Categoria')
		verbose_name_plural = _('Categorias')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)



#Cada categoria puede tener varias subcategorias 
# para que las busquedas sean especificas
class Sub_categoria(models.Model):
	Categoria = models.ForeignKey(Categoria)
	nombre =models.CharField(max_length=30, verbose_name=_('Sub Categoria'))
	class Meta:
		verbose_name = _('Sub Categoria')
		verbose_name_plural = _('Sub Categorias')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)





