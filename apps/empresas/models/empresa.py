# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
# Api de manejo de imagen
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill

from apps.empresas.models.BDlocalidades import Localidades



from django.utils.translation import ugettext_lazy as _
#from django_localflavor_mx.models import MXStateField, MXZipCodeField, 
# MXCURPField


	
# Metodo para  generar la ruta donde se guardaran los logos
def get_image_path(empresa, filename):
	return os.path.join('imagenes/empresas/'+str(empresa.id), 'logos', filename)




## Cada servicio puede tener diferentes tags que vamos a utilizar cuando se crea una promocion.
#class Sub_categoria(models.Model):
class Tags(models.Model):
	nombre =models.CharField(max_length=30,
			 verbose_name=_('Nombre del Tag'))
	class Meta:
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)




#Modelo para crear las categorias, deben ser iguales a Google places [Types]
class Categoria(models.Model):
	nombre_ingles =models.CharField(max_length=30, default='none',unique=True
				 ,verbose_name=_('Categoria Ingles'))
	nombre =models.CharField(max_length=30, verbose_name=_('Categoria'))
	tags = models.ManyToManyField("Tags",null = True)
	class Meta:
		verbose_name = _('Categoria')
		verbose_name_plural = _('Categorias')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)



### Falta agregar el campo para logo de la empresa 
class Empresa(models.Model):
	matriz = models.ForeignKey('self',null=True)
	empresa_user = models.ForeignKey(User) ## Verificar el por que de este campo
	nombre = models.CharField(max_length=50, 
				verbose_name=_('Nombre de la empresa'))
	giro = models.ForeignKey('Categoria', null=True)
	telefono = models.CharField(max_length=15, blank=True)
	rfc = models.CharField(max_length=15, unique=True)
	email = models.EmailField(null=True, blank=True, 
				verbose_name=_('Correo electronico'))
	sitio_web = models.URLField(null=True,blank=True,
				verbose_name=_('Sitio web'))
	localidad = models.ForeignKey('Localidades', null=True)
	direccion  = models.CharField(max_length=90, verbose_name=_('Direccion'))
	fecha_alta = models.DateTimeField(auto_now=True)
	LatLng = models.CharField(max_length=60, blank=True)
	is_active = models.BooleanField(default=False) 
	codigo_confirmacion = models.CharField(max_length=32, blank=True)
	total_capital =  models.DecimalField(max_digits=7, decimal_places=2,
											default=0.0)
	reference_place =  models.CharField(max_length=255, blank=True)
	id_place = models.CharField(max_length=48, blank=True)
	class Meta:
		app_label = 'empresas'
		verbose_name = _('Empresa')
		verbose_name_plural = _('Empresas')

	def __unicode__(self):
		return '%s' %(self.nombre)

# Se crea esta tabla para vincular los encargados que pueda tener una empresa
#******* Verificar  si puede ser un campo many to many
class Encargados_empresas(models.Model):
	user = models.ForeignKey(User)
	empresa = models.ForeignKey(Empresa)

	class Meta:
		app_label = 'empresas'
		verbose_name = _('Encargado_empresa')
		verbose_name_plural = _('Encargados_empresas')







