# -*- coding: utf-8 *-*
from django.db import models

from apps.cupones.models.cupon import Cupon
from apps.empresas.models.empresa import Empresa


from django.utils.translation import ugettext_lazy as _


CONCEPTOS = (
	('1', _('Inscripcion')),
	('0', _('Mensualidad')),
)
FORMASPAGO = (
	('1', _('Contado')),
	('0', _('Credito')),
)


### Este modelo se utiliza para guardar todos los depositos que haga la empresa
class capitalEmpresaDeposito(models.Model):
	empresa = models.ForeignKey(Empresa)
	fecha_deposito = models.DateTimeField(auto_now=True)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2,default=0.0,
									verbose_name=_(u'Monto a pagar $'))
	formaPago = models.CharField(max_length=1, choices=FORMASPAGO, 
								verbose_name=_('Forma de pago'), default='0')
	verificado= models.BooleanField(default=False, blank=True)
	def __unicode__(self):
		return u'Fecha: %s - Monto: %s' % (self.fecha_deposito, 
														self.cantidad)

	class Meta:
		app_label = 'pagos'




### Este modelo se utiliza para cobrar la comision por cada venta realizada.
class cobroCuponComision(models.Model):
	cupon = models.ForeignKey(Cupon)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2,default=0.0,
									verbose_name=_(u'Monto a pagar $'))
	class Meta:
		verbose_name = _('Pago del cupon')
		verbose_name_plural = _('Pago de cupones')
		app_label= 'pagos'
	def __unicode__(self):
		return '%s' %(self.num_folio)



### Este modelo se utiliza para cobrear la membresia mensual de cada empresa
class pagoEmpresaMembresia(models.Model):
	empresa = models.ForeignKey(Empresa)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2,default=0.0,
									verbose_name=_(u'Monto a pagar $'))
	fecha_pago = models.DateTimeField(auto_now=True)
	concepto = models.CharField(max_length=1, choices=CONCEPTOS, 
								verbose_name=_('Concepto de pago'), default='1')
	def __unicode__(self):
		return u'Empresa: %s - Fecha de pago: %s' % (self.empresa, 
														self.fecha_pago)

	class Meta:
		app_label = 'pagos'


		
