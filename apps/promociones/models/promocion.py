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
	tipo_promocion =models.CharField(choices=tipo_promocion_choices,default='des'
						,max_length=3,verbose_name=(u'Tipo de promocion'))
	des_tipoPromo = models.CharField(max_length=60, blank=True,
						verbose_name=(u'Descripcion'))
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateField(blank=True,default='2010-01-01',
						verbose_name=_('Fecha de publicacion'))
	fecha_termino = models.DateField(blank=True,default='2010-01-01',
						verbose_name=_('Fecha limite'))
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES,
						verbose_name=_('Estado'), default='0')
	imagen = models.ImageField(upload_to=get_image_path, 
						verbose_name='Imagen promocion')
	total_promociones = models.CharField(max_length=27,default="-")
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
	

	