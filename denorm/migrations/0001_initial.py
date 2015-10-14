# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DenormModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('ham', models.TextField(editable=False)),
                ('spam', models.TextField(editable=False)),
            ],
            options={
                'abstract': False,
                'swappable': 'DENORM_MODEL',
            },
        ),
        migrations.CreateModel(
            name='DirtyInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.TextField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='RealDenormModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('ham', models.TextField(editable=False)),
                ('eggs', models.TextField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
