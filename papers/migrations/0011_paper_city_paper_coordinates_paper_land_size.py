# Generated by Django 5.1.4 on 2024-12-27 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0010_remove_paper_transaction_hash_alter_paper_ipfs_hash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='city',
            field=models.CharField(default=datetime.datetime(24, 12, 28, 0, 0), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='coordinates',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='land_size',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Enter the land size in acres/hectares/etc.', max_digits=10),
            preserve_default=False,
        ),
    ]
