# Generated by Django 5.1.4 on 2024-12-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_alter_paper_ipfs_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='user',
            field=models.CharField(max_length=256),
        ),
    ]
