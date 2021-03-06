# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'capitalEmpresaDeposito'
        db.create_table(u'pagos_capitalempresadeposito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('fecha_deposito', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('formaPago', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('verificado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pagos', ['capitalEmpresaDeposito'])

        # Adding model 'cobroCuponComision'
        db.create_table(u'pagos_cobrocuponcomision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cupon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cupones.Cupon'])),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('pagos', ['cobroCuponComision'])

        # Adding model 'pagoEmpresaMembresia'
        db.create_table(u'pagos_pagoempresamembresia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('fecha_pago', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('concepto', self.gf('django.db.models.fields.CharField')(default='1', max_length=1)),
        ))
        db.send_create_signal('pagos', ['pagoEmpresaMembresia'])


    def backwards(self, orm):
        # Deleting model 'capitalEmpresaDeposito'
        db.delete_table(u'pagos_capitalempresadeposito')

        # Deleting model 'cobroCuponComision'
        db.delete_table(u'pagos_cobrocuponcomision')

        # Deleting model 'pagoEmpresaMembresia'
        db.delete_table(u'pagos_pagoempresamembresia')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_tarjeta': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['usuarios.Tarjeta']", 'through': "orm['usuarios.userTarjeta']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cupones.cupon': {
            'Meta': {'object_name': 'Cupon'},
            'canjeado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empleado_atend': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'fecha_canjeado': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_solicitud': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_folio': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promociones.Promocion']"}),
            'tipo_user_tarjeta': ('django.db.models.fields.CharField', [], {'default': "'pr'", 'max_length': '2'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'empresas.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'empresas.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'encargado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'giro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitud_mapa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud_mapa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'num_interior': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'total_capital': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2'})
        },
        'empresas.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'estado': ('django.db.models.fields.CharField', [], {'default': "'PUE'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'empresas.sub_categoria': {
            'Categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Categoria']"}),
            'Meta': {'object_name': 'Sub_categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'pagos.capitalempresadeposito': {
            'Meta': {'object_name': 'capitalEmpresaDeposito'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Empresa']"}),
            'fecha_deposito': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'formaPago': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'verificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'pagos.cobrocuponcomision': {
            'Meta': {'object_name': 'cobroCuponComision'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'cupon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupones.Cupon']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pagos.pagoempresamembresia': {
            'Meta': {'object_name': 'pagoEmpresaMembresia'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'concepto': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Empresa']"}),
            'fecha_pago': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'promociones.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['empresas.Sub_categoria']", 'symmetrical': 'False'}),
            'des_tipoPromo': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'descuento': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Empresa']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_publicacion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'precio_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'tipo_promocion': ('django.db.models.fields.CharField', [], {'default': "'des'", 'max_length': '3'}),
            'titulo_promocion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'usuarios.tarjeta': {
            'Meta': {'object_name': 'Tarjeta'},
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_tarjera': ('django.db.models.fields.CharField', [], {'default': "'pr'", 'max_length': '2'})
        },
        'usuarios.usertarjeta': {
            'Meta': {'object_name': 'userTarjeta'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_baja': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tarjeta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['usuarios.Tarjeta']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['pagos']