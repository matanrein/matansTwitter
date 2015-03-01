# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matansTwitter', '0004_auto_20150228_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followed',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30)),
                ('followers', models.ManyToManyField(to='matansTwitter.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
