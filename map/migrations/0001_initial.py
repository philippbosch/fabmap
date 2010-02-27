
from south.db import db
from django.db import models
from map.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('map_location', (
            ('id', orm['map.Location:id']),
            ('type', orm['map.Location:type']),
            ('location_name', orm['map.Location:location_name']),
            ('contact_name', orm['map.Location:contact_name']),
            ('address', orm['map.Location:address']),
            ('latitude', orm['map.Location:latitude']),
            ('longitude', orm['map.Location:longitude']),
            ('website', orm['map.Location:website']),
            ('twitter', orm['map.Location:twitter']),
            ('description', orm['map.Location:description']),
        ))
        db.send_create_signal('map', ['Location'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('map_location')
        
    
    
    models = {
        'map.location': {
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['map']
