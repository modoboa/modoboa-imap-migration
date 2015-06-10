# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modoboa_admin', '0003_domain_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Migration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_password', models.CharField(max_length=100)),
                ('mailbox', models.ForeignKey(to='modoboa_admin.Mailbox')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
