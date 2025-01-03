# Generated by Django 5.0.7 on 2024-07-18 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account_number', models.BigIntegerField()),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('alpha2_code', models.CharField(max_length=2)),
                ('alpha3_code', models.CharField(max_length=3)),
                ('country_name', models.CharField(max_length=100)),
                ('numeric_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VerificationLevel',
            fields=[
                ('level_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('birthday', models.DateTimeField()),
                ('city', models.CharField(max_length=255)),
                ('internal_type', models.CharField(max_length=50)),
                ('locale', models.CharField(max_length=50)),
                ('risk_level', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('logged_at', models.DateTimeField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('tags', models.JSONField()),
                ('analytics', models.JSONField()),
                ('accounts', models.ManyToManyField(to='clients.account')),
                ('client_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clienttype')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.company')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.country')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.manager')),
                ('verification_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.verificationlevel')),
            ],
        ),
    ]
