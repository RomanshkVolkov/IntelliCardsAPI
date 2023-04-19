# Generated by Django 4.1.8 on 2023-04-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=255)),
                ('insertion', models.CharField(max_length=255)),
                ('innervation', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'muscles',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('muscles', models.ManyToManyField(to='muscles.muscle')),
            ],
            options={
                'db_table': 'folders',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('folders', models.ManyToManyField(to='muscles.folder')),
            ],
            options={
                'db_table': 'custom_users',
            },
        ),
    ]
