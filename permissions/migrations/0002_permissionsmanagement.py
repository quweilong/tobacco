# Generated by Django 2.2.6 on 2019-12-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionsManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('permissions_id', models.IntegerField()),
                ('parent_permissions_id', models.IntegerField()),
                ('permissions_name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
