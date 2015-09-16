# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Education'
        db.create_table(u'resume_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.User'], unique=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(default='Bachelor', max_length=8, blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'resume', ['Education'])

        # Adding model 'Experience'
        db.create_table(u'resume_experience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.User'], unique=True)),
            ('activity', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('internship', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('awards', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('association', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('other', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'resume', ['Experience'])

        # Adding model 'Resume'
        db.create_table(u'resume_resume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.User'], unique=True)),
            ('info', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.Info'], unique=True)),
            ('education', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['resume.Education'], unique=True)),
            ('experience', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['resume.Experience'], unique=True)),
        ))
        db.send_create_signal(u'resume', ['Resume'])


    def backwards(self, orm):
        # Deleting model 'Education'
        db.delete_table(u'resume_education')

        # Deleting model 'Experience'
        db.delete_table(u'resume_experience')

        # Deleting model 'Resume'
        db.delete_table(u'resume_resume')


    models = {
        u'account.info': {
            'Meta': {'object_name': 'Info'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.User']", 'unique': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friends_rel_+'", 'null': 'True', 'to': u"orm['account.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        u'resume.education': {
            'Meta': {'object_name': 'Education'},
            'degree': ('django.db.models.fields.CharField', [], {'default': "'Bachelor'", 'max_length': '8', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.User']", 'unique': 'True'})
        },
        u'resume.experience': {
            'Meta': {'object_name': 'Experience'},
            'activity': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'association': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'awards': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internship': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.User']", 'unique': 'True'})
        },
        u'resume.resume': {
            'Meta': {'object_name': 'Resume'},
            'education': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['resume.Education']", 'unique': 'True'}),
            'experience': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['resume.Experience']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.Info']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['resume']