# Generated by Django 3.1.3 on 2023-12-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0009_test_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
