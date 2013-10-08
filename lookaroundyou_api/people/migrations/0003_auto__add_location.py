# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'people_location', (
            ('id', self.gf('lookaroundyou_api.common.fields.StringUUIDField')(unique=True, max_length=32, primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('altitude', self.gf('django.db.models.fields.FloatField')()),
            ('horizontal_accuracy', self.gf('django.db.models.fields.FloatField')()),
            ('vertical_accuracy', self.gf('django.db.models.fields.FloatField')()),
            ('course', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('speed', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('measured_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'people', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'people_location')


    models = {
        u'people.location': {
            'Meta': {'object_name': 'Location'},
            'altitude': ('django.db.models.fields.FloatField', [], {}),
            'course': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'horizontal_accuracy': ('django.db.models.fields.FloatField', [], {}),
            'id': ('lookaroundyou_api.common.fields.StringUUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'measured_at': ('django.db.models.fields.DateTimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vertical_accuracy': ('django.db.models.fields.FloatField', [], {})
        },
        u'people.person': {
            'Meta': {'object_name': 'Person'},
            'apns_token': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('lookaroundyou_api.common.fields.StringUUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'send_push_notifications': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['people']