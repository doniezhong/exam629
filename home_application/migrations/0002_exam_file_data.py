# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='file_data',
            field=models.BinaryField(default=b''),
            preserve_default=False,
        ),
    ]
