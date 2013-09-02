# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Empresa.reference_place'
        db.alter_column(u'empresas_empresa', 'reference_place', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Empresa.reference_place'
        db.alter_column(u'empresas_empresa', 'reference_place', self.gf('django.db.models.fields.CharField')(max_length=155))

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
        'empresas.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre_ingles': ('django.db.models.fields.CharField', [], {'default': "'none'", 'unique': 'True', 'max_length': '30'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['empresas.Tags']", 'null': 'True', 'symmetrical': 'False'})
        },
        'empresas.empresa': {
            'LatLng': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'Meta': {'object_name': 'Empresa'},
            'codigo_confirmacion': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empresa_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'giro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Categoria']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_place': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Localidades']", 'null': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reference_place': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rfc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'total_capital': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2'})
        },
        'empresas.encargados_empresas': {
            'Meta': {'object_name': 'Encargados_empresas'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'empresas.estados': {
            'Meta': {'object_name': 'Estados'},
            'abrev': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        'empresas.localidades': {
            'Meta': {'object_name': 'Localidades'},
            'altitud': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Municipios']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '110'})
        },
        'empresas.municipios': {
            'Meta': {'object_name': 'Municipios'},
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Estados']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'empresas.tags': {
            'Meta': {'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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

    complete_apps = ['empresas']