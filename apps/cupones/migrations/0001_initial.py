# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cupon'
        db.create_table(u'cupones_cupon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promociones.Promocion'])),
            ('num_folio', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('canjeado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_solicitud', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('fecha_canjeado', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tipo_user_tarjeta', self.gf('django.db.models.fields.CharField')(default='pr', max_length=2)),
        ))
        db.send_create_signal('cupones', ['Cupon'])


    def backwards(self, orm):
        # Deleting model 'Cupon'
        db.delete_table(u'cupones_cupon')


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
            'fecha_canjeado': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_solicitud': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_folio': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promociones.Promocion']"}),
            'tipo_user_tarjeta': ('django.db.models.fields.CharField', [], {'default': "'pr'", 'max_length': '2'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'empresas.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'encargado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'giro': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud_mapa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud_mapa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'num_interior': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'empresas.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'estado': ('django.db.models.fields.CharField', [], {'default': "'PUE'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'promociones.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Empresa']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_publicacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'precio_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'titulo_promocion': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['cupones']