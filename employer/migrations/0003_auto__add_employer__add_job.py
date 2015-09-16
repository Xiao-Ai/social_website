# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employer'
        db.create_table(u'employer_employer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('corporation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=18)),
        ))
        db.send_create_signal(u'employer', ['Employer'])

        # Adding M2M table for field employees on 'Employer'
        m2m_table_name = db.shorten_name(u'employer_employer_employees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employer', models.ForeignKey(orm[u'employer.employer'], null=False)),
            ('user', models.ForeignKey(orm[u'account.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employer_id', 'user_id'])

        # Adding model 'Job'
        db.create_table(u'employer_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Employer'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('requirement', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('others', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'employer', ['Job'])


    def backwards(self, orm):
        # Deleting model 'Employer'
        db.delete_table(u'employer_employer')

        # Removing M2M table for field employees on 'Employer'
        db.delete_table(db.shorten_name(u'employer_employer_employees'))

        # Deleting model 'Job'
        db.delete_table(u'employer_job')


    models = {
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friends_rel_+'", 'null': 'True', 'to': u"orm['account.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        u'employer.employer': {
            'Meta': {'object_name': 'Employer'},
            'corporation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'employees': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['account.User']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        u'employer.job': {
            'Meta': {'object_name': 'Job'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Employer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'others': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'requirement': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['employer']