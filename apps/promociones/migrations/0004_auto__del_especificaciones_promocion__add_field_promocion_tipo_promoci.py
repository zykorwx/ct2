# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Especificaciones_promocion'
        db.delete_table(u'promociones_especificaciones_promocion')

        # Adding field 'Promocion.tipo_promocion'
        db.add_column(u'promociones_promocion', 'tipo_promocion',
                      self.gf('django.db.models.fields.CharField')(default='des', max_length=3),
                      keep_default=False)

        # Adding field 'Promocion.des_tipoPromo'
        db.add_column(u'promociones_promocion', 'des_tipoPromo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Promocion.total_promociones'
        db.add_column(u'promociones_promocion', 'total_promociones',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=27),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Especificaciones_promocion'
        db.create_table(u'promociones_especificaciones_promocion', (
            ('num_max_platino', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('descuento_porcentaje', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('num_max_golden', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('num_max_premier', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promociones.Promocion'])),
            ('tipo_promocion', self.gf('django.db.models.fields.CharField')(default='des', max_length=3)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_max_preferente', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('promociones', ['Especificaciones_promocion'])

        # Deleting field 'Promocion.tipo_promocion'
        db.delete_column(u'promociones_promocion', 'tipo_promocion')

        # Deleting field 'Promocion.des_tipoPromo'
        db.delete_column(u'promociones_promocion', 'des_tipoPromo')

        # Deleting field 'Promocion.total_promociones'
        db.delete_column(u'promociones_promocion', 'total_promociones')


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
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'default': "'2013-07-07 17:27:17'", 'auto_now': 'True', 'blank': 'True'}),
            'giro': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
        'promociones.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'promociones.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['promociones.Sub_categoria']", 'symmetrical': 'False'}),
            'des_tipoPromo': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresas.Empresa']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_publicacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'precio_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'tipo_promocion': ('django.db.models.fields.CharField', [], {'default': "'des'", 'max_length': '3'}),
            'titulo_promocion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'total_promociones': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '27'})
        },
        'promociones.sub_categoria': {
            'Categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promociones.Categoria']"}),
            'Meta': {'object_name': 'Sub_categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['promociones']