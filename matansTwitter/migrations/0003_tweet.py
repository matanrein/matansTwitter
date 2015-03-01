# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matansTwitter', '0002_auto_20150228_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tweet_id', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
