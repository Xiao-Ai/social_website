# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field employees on 'Job'
        m2m_table_name = db.shorten_name(u'employer_job_employees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm[u'employer.job'], null=False)),
            ('user', models.ForeignKey(orm[u'account.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'user_id'])


    def backwards(self, orm):
        # Removing M2M table for field employees on 'Job'
        db.delete_table(db.shorten_name(u'employer_job_employees'))


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        u'employer.job': {
            'Meta': {'object_name': 'Job'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'applicants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'applicants'", 'blank': 'True', 'to': u"orm['account.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'employees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'employees'", 'blank': 'True', 'to': u"orm['account.User']"}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Employer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'others': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'requirement': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['employer']