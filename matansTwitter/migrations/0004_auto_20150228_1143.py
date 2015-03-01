# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matansTwitter', '0003_tweet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='text',
            new_name='tweet_text',
        ),
    ]
