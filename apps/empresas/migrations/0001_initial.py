# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Municipio'
        db.create_table(u'empresas_municipio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(default='PUE', max_length=3)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('empresas', ['Municipio'])

        # Adding model 'Empresa'
        db.create_table(u'empresas_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('giro', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('sitio_web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Municipio'])),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('num_exterior', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('num_interior', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('encargado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('latitud_mapa', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud_mapa', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('empresas', ['Empresa'])


    def backwards(self, orm):
        # Deleting model 'Municipio'
        db.delete_table(u'empresas_municipio')

        # Deleting model 'Empresa'
        db.delete_table(u'empresas_empresa')


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
        }
    }

    complete_apps = ['empresas']