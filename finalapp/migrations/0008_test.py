# Generated by Django 3.1.3 on 2023-12-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0007_auto_20231207_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hos', models.IntegerField()),
                ('pop', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
