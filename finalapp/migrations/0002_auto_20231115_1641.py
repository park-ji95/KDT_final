# Generated by Django 3.1.3 on 2023-11-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.TextField()),
                ('clinic', models.IntegerField()),
                ('healthcenter', models.IntegerField()),
                ('pharmacy', models.IntegerField()),
                ('dentist', models.IntegerField()),
                ('oriental', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=255)),
                ('hospital', models.IntegerField()),
                ('doctor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicalinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('hospital', models.IntegerField()),
                ('doctor', models.IntegerField()),
                ('nurse', models.IntegerField()),
                ('patient', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.TextField(max_length=10)),
                ('m1', models.IntegerField()),
                ('m2', models.IntegerField()),
                ('m3', models.IntegerField()),
                ('m4', models.IntegerField()),
                ('m5', models.IntegerField()),
                ('m6', models.IntegerField()),
                ('m7', models.IntegerField()),
                ('m8', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.TextField()),
                ('total', models.IntegerField()),
                ('m', models.IntegerField()),
                ('f', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Sejong',
        ),
    ]
