# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Notification.event'
        db.add_column(u'notifications_notification', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Notification.location'
        db.add_column(u'notifications_notification', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Location'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Notification.event'
        db.delete_column(u'notifications_notification', 'event_id')

        # Deleting field 'Notification.location'
        db.delete_column(u'notifications_notification', 'location_id')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('lookaroundyou_api.common.fields.StringUUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'radius': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'notifications.notification': {
            'Meta': {'object_name': 'Notification'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('lookaroundyou_api.common.fields.StringUUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Location']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'people.location': {
            'Meta': {'object_name': 'Location'},
            'altitude': ('django.db.models.fields.FloatField', [], {}),
            'course': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'horizontal_accuracy': ('django.db.models.fields.FloatField', [], {}),
            'id': ('lookaroundyou_api.common.fields.StringUUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'measured_at': ('django.db.models.fields.DateTimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['people.Person']"}),
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

    complete_apps = ['notifications']