
from south.db import db
from django.db import models
from map.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Location.longitude'
        # (to signature: django.db.models.fields.FloatField(null=True, blank=True))
        db.alter_column('map_location', 'longitude', orm['map.location:longitude'])
        
        # Changing field 'Location.latitude'
        # (to signature: django.db.models.fields.FloatField(null=True, blank=True))
        db.alter_column('map_location', 'latitude', orm['map.location:latitude'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Location.longitude'
        # (to signature: django.db.models.fields.FloatField(blank=True))
        db.alter_column('map_location', 'longitude', orm['map.location:longitude'])
        
        # Changing field 'Location.latitude'
        # (to signature: django.db.models.fields.FloatField(blank=True))
        db.alter_column('map_location', 'latitude', orm['map.location:latitude'])
        
    
    
    models = {
        'map.location': {
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['map']
