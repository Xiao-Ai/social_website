# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Employer'
        db.delete_table(u'employer_employer')

        # Removing M2M table for field employee on 'Employer'
        db.delete_table(db.shorten_name(u'employer_employer_employee'))


    def backwards(self, orm):
        # Adding model 'Employer'
        db.create_table(u'employer_employer', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True)),
        ))
        db.send_create_signal(u'employer', ['Employer'])

        # Adding M2M table for field employee on 'Employer'
        m2m_table_name = db.shorten_name(u'employer_employer_employee')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employer', models.ForeignKey(orm[u'employer.employer'], null=False)),
            ('user', models.ForeignKey(orm[u'account.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employer_id', 'user_id'])


    models = {
        
    }

    complete_apps = ['employer']