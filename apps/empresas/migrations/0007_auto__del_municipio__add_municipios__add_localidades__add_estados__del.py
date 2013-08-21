# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Municipio'
        db.delete_table(u'empresas_municipio')

        # Adding model 'Municipios'
        db.create_table(u'empresas_municipios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Estados'])),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('empresas', ['Municipios'])

        # Adding model 'Localidades'
        db.create_table(u'empresas_localidades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Municipios'])),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=110)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('latitud', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('longitud', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('altitud', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('empresas', ['Localidades'])

        # Adding model 'Estados'
        db.create_table(u'empresas_estados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('abrev', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('empresas', ['Estados'])

        # Deleting field 'Empresa.num_interior'
        db.delete_column(u'empresas_empresa', 'num_interior')

        # Deleting field 'Empresa.colonia'
        db.delete_column(u'empresas_empresa', 'colonia')

        # Deleting field 'Empresa.municipio'
        db.delete_column(u'empresas_empresa', 'municipio_id')

        # Adding field 'Empresa.localidad'
        db.add_column(u'empresas_empresa', 'localidad',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Localidades'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Municipio'
        db.create_table(u'empresas_municipio', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('estado', self.gf('django.db.models.fields.CharField')(default='PUE', max_length=3)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('empresas', ['Municipio'])

        # Deleting model 'Municipios'
        db.delete_table(u'empresas_municipios')

        # Deleting model 'Localidades'
        db.delete_table(u'empresas_localidades')

        # Deleting model 'Estados'
        db.delete_table(u'empresas_estados')

        # Adding field 'Empresa.num_interior'
        db.add_column(u'empresas_empresa', 'num_interior',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True),
                      keep_default=False)

        # Adding field 'Empresa.colonia'
        db.add_column(u'empresas_empresa', 'colonia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Empresa.municipio'
        db.add_column(u'empresas_empresa', 'municipio',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Municipio'], null=True),
                      keep_default=False)

        # Deleting field 'Empresa.localidad'
        db.delete_column(u'empresas_empresa', 'localidad_id')


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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'empresas.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'codigo_confirmacion': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empresa_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'giro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Categoria']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitud_mapa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Localidades']", 'null': 'True'}),
            'longitud_mapa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '110'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'empresas.municipios': {
            'Meta': {'object_name': 'Municipios'},
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Estados']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'empresas.sub_categoria': {
            'Categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Categoria']"}),
            'Meta': {'object_name': 'Sub_categoria'},
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