# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models.empresa import Empresa
import os
from django.utils.translation import ugettext_lazy as _

# Se usa para usarlo en un combo
ESTADO_CHOICES = (
	('1', _('Publicar')),
	('0', _('Suspende Temporalmente')),
)

tipo_promocion_choices = [('des','Descuento'),('pxt','Producto extra')]


def get_image_path(promocion, filename):
	return os.path.join('imagenes/empresas/emp_'+str(promocion.empresa), 'promociones', filename)


#Modelo para crear las categorias a las que van a pertenecer las proociones
class Categoria(models.Model):
	nombre =models.CharField(max_length=30, verbose_name=_('Categoria'))
	class Meta:
		verbose_name = _('Categoria')
		verbose_name_plural = _('Categorias')
		app_label = 'promociones'
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
		app_label = 'promociones'
	def __unicode__(self):
		return '%s' %(self.nombre)



class Promocion(models.Model):
	empresa = models.ForeignKey(Empresa)
	categoria = models.ManyToManyField(Sub_categoria)
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateField(blank=True, null=True, 
						verbose_name=_('Fecha de publicacion'))
	fecha_termino = models.DateField(blank=True, null=True, 
						verbose_name=_('Fecha limite'))
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES,
						verbose_name=_('Estado'), default='0')
	imagen = models.ImageField(upload_to=get_image_path, 
						verbose_name='Imagen promocion')
	
	titulo_promocion = models.CharField(max_length=30,verbose_name=_('Titulo'))
	descripcion = models.TextField(verbose_name=_('Descripcion'))
	precio_total =  models.DecimalField(max_digits=6, decimal_places=2, 
						verbose_name=_(u'Precio'))
	class Meta:
		verbose_name = _('Promocion')
		verbose_name_plural = _('Promociones')
		app_label='promociones'
	def __unicode__(self):
		return '%s' %(self.titulo_promocion)
	

class Especificaciones_promocion(models.Model):
	promocion = models.ForeignKey(Promocion)
	tipo_promocion =models.CharField(choices=tipo_promocion_choices,default='des'
						,max_length=3,verbose_name=(u'Tipo de promocion'))
	descripcion = models.CharField(max_length=60, blank=True,
						verbose_name=(u'Descripcion'))
	descuento_porcentaje = models.PositiveSmallIntegerField( 
						verbose_name=(u'Porcentaje de descuento'))
	num_max_preferente = models.PositiveSmallIntegerField(
						verbose_name=(u'Preferente'))
	num_max_platino = models.PositiveSmallIntegerField(
						verbose_name=(u'Platino'))
	num_max_golden = models.PositiveSmallIntegerField(
						verbose_name=(u'Golden'))
	num_max_premier = models.PositiveSmallIntegerField(
						verbose_name=(u'Premier'))

	class Meta:
		verbose_name = _('Caracteristicas de la promocion')
		verbose_name_plural = _('Caracteristicas de las promociones')
		app_label='promociones'
	def __unicode__(self):
		return '%s' %(self.tipo_promocion)
	
	