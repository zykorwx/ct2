# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comentario_promocion'
        db.create_table(u'comentarios_comentario_promocion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promociones.Promocion'])),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('comentarios', ['Comentario_promocion'])

        # Adding model 'Calificacion_comentario'
        db.create_table(u'comentarios_calificacion_comentario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comentario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comentarios.Comentario_promocion'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('calificacion', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('comentarios', ['Calificacion_comentario'])

        # Adding model 'Preguntas_promocion'
        db.create_table(u'comentarios_preguntas_promocion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal('comentarios', ['Preguntas_promocion'])

        # Adding model 'Calificacion_promocion'
        db.create_table(u'comentarios_calificacion_promocion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promociones.Promocion'])),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comentarios.Preguntas_promocion'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('calificacion', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('comentarios', ['Calificacion_promocion'])


    def backwards(self, orm):
        # Deleting model 'Comentario_promocion'
        db.delete_table(u'comentarios_comentario_promocion')

        # Deleting model 'Calificacion_comentario'
        db.delete_table(u'comentarios_calificacion_comentario')

        # Deleting model 'Preguntas_promocion'
        db.delete_table(u'comentarios_preguntas_promocion')

        # Deleting model 'Calificacion_promocion'
        db.delete_table(u'comentarios_calificacion_promocion')


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
        'comentarios.calificacion_comentario': {
            'Meta': {'object_name': 'Calificacion_comentario'},
            'calificacion': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'comentario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comentarios.Comentario_promocion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'comentarios.calificacion_promocion': {
            'Meta': {'object_name': 'Calificacion_promocion'},
            'calificacion': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comentarios.Preguntas_promocion']"}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promociones.Promocion']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'comentarios.comentario_promocion': {
            'Meta': {'object_name': 'Comentario_promocion'},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promociones.Promocion']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'comentarios.preguntas_promocion': {
            'Meta': {'object_name': 'Preguntas_promocion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '45'})
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

    complete_apps = ['comentarios']