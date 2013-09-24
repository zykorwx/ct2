# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models.empresa import Empresa, Categoria, Tags
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








### Modificar el campo imagen para que acepte varias eimagenes...
#**************************************************
class Promocion(models.Model):
	empresa = models.ForeignKey(Empresa)
	categoria = models.ManyToManyField(Tags)
	tipo_promocion =models.CharField(choices=tipo_promocion_choices,default='des'
						,max_length=3,verbose_name=(u'Tipo de promocion'))
	des_tipoPromo = models.CharField(max_length=140, blank=True,
						verbose_name=(u'Descripcion'))
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateField(blank=True,
						verbose_name=_('Fecha de publicacion'))
	fecha_termino = models.DateField(blank=True,
						verbose_name=_('Fecha limite'))
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES,
						verbose_name=_('Estado'), default='0')
	imagen = models.ImageField(upload_to=get_image_path, 
						verbose_name='Imagen promocion')
	titulo_promocion = models.CharField(max_length=30,verbose_name=_('Titulo'))
	descripcion = models.CharField(max_length=140,verbose_name=_('Descripcion'))
	precio_total =  models.DecimalField(max_digits=6, decimal_places=2, 
						verbose_name=_(u'Precio'))
	descuento = models.PositiveSmallIntegerField(default=5,
				verbose_name=u'Porcentaje de descuento')
	tiposDescuentos = models.CharField(max_length=110,blank= True)
 	class Meta:
		verbose_name = _('Promocion')
		verbose_name_plural = _('Promociones')
		app_label='promociones'
	def __unicode__(self):
		return '%s' %(self.titulo_promocion)
	



	