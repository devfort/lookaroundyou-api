# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.altitude'
        db.alter_column(u'people_location', 'altitude', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Location.altitude'
        db.alter_column(u'people_location', 'altitude', self.gf('django.db.models.fields.FloatField')(default=0))

    models = {
        u'people.location': {
            'Meta': {'object_name': 'Location'},
            'altitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'horizontal_accuracy': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('lookaroundyou_api.common.fields.StringUUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'measured_at': ('django.db.models.fields.DateTimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['people.Person']"}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vertical_accuracy': ('django.db.models.fields.FloatField', [], {'default': '0'})
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