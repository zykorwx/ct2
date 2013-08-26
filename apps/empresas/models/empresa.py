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



choices_giro = [('ali','Alimentos'),('dep','Deportes'),('sal','Salud')]




	
	# Metodo para  generar la ruta donde se guardaran los logos
def get_image_path(empresa, filename):
    return os.path.join('imagenes/empresas/'+str(empresa.id), 'logos', filename)

### Falta agregar el campo para logo de la empresa 
class Empresa(models.Model):
	empresa_user = models.ForeignKey(User)
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
	###colonia = models.CharField(blank=True, max_length=70, verbose_name=_('Colonia'))
	direccion  = models.CharField(max_length=90, verbose_name=_('Direccion'))
	fecha_alta = models.DateTimeField(auto_now=True)
	LatLng = models.CharField(max_length=60, blank=True)
	is_active = models.BooleanField(default=False) 
	codigo_confirmacion = models.CharField(max_length=32, blank=True)
	total_capital =  models.DecimalField(max_digits=7, decimal_places=2,
											default=0.0)
	reference_place =  models.CharField(max_length=155, blank=True)
	id_place = models.CharField(max_length=48, blank=True)
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
	nombre_ingles =models.CharField(max_length=30, default='none',unique=True
				 ,verbose_name=_('Categoria Ingles'))
	nombre =models.CharField(max_length=30, verbose_name=_('Categoria'))
	class Meta:
		verbose_name = _('Categoria')
		verbose_name_plural = _('Categorias')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)



#Cada categoria puede tener varias subcategorias 
# para que las busquedas sean especificas
#Elimine la referencia con categoria por la forma en la que organiza google 
#ya no es necesario, las subcategorias serian por productos solamente
#y ya no por empresa.
class Sub_categoria(models.Model):
	nombre =models.CharField(max_length=30,default='none',
			 verbose_name=_('Sub Categoria'))
	class Meta:
		verbose_name = _('Sub Categoria')
		verbose_name_plural = _('Sub Categorias')
		app_label = 'empresas'
	def __unicode__(self):
		return '%s' %(self.nombre)





