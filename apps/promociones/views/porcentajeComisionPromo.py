# -*- coding: utf-8 *-*
porcentajeComision = 0.05

""" A continuacion voy a poner las variables para 
	lo que van a ser los tipos de tarjetas por ejemplo
	cuantas compras como minimo debe tener el usuario
	para ser preferente, cuantas para platino, cuantas 
	para golden y por ultimo cuantas para premier
 """

Preferente = 5 ### de 0 a 5 compras va a ser preferente
Platino = 10	### si ya hizo mas de 5 compras pero menos de 11 
Golden = 15	### Si ya hizo mas de 10 pero menos de 16
Premier = 20	### Si ya hizo mas de 15 compras sera premier

"""La siguiente variable se va a utilizar para saber la proporcion
	en el aumento del descuento, es decir si la empresa xxx en su 
	promoción "Promo 23 ft" puso que el descuento inicial (descuento
	para tarjetas tipo # Preferente # va a ser del 5% sobre el costo
	del producto) con la variable aumentoDescuento vamos a saber
	que entonces el descuento para tarjetas de tipo 
	Platino = desceuntoInicial + aumentoDescuento
	Golden  = desceuntoInicial + (aumentoDescuento * 2)
	Premier = desceuntoInicial + (aumentoDescuento * 3)
"""
aumentoDescuento = 5