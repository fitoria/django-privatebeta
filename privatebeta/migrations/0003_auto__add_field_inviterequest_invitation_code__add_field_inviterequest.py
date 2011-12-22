# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'InviteRequest.invitation_code'
        db.add_column('privatebeta_inviterequest', 'invitation_code', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True, null=True), keep_default=False)

        # Adding field 'InviteRequest.invited_date'
        db.add_column('privatebeta_inviterequest', 'invited_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'InviteRequest.used_invitation'
        db.add_column('privatebeta_inviterequest', 'used_invitation', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'InviteRequest.used_invitation_date'
        db.add_column('privatebeta_inviterequest', 'used_invitation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'InviteRequest.invitation_code'
        db.delete_column('privatebeta_inviterequest', 'invitation_code')

        # Deleting field 'InviteRequest.invited_date'
        db.delete_column('privatebeta_inviterequest', 'invited_date')

        # Deleting field 'InviteRequest.used_invitation'
        db.delete_column('privatebeta_inviterequest', 'used_invitation')

        # Deleting field 'InviteRequest.used_invitation_date'
        db.delete_column('privatebeta_inviterequest', 'used_invitation_date')


    models = {
        'privatebeta.inviterequest': {
            'Meta': {'object_name': 'InviteRequest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True', 'null': 'True'}),
            'invited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invited_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'used_invitation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'used_invitation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['privatebeta']
