# Generated by Django 4.0.5 on 2022-07-09 22:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField()),
                ('company_name', models.CharField(max_length=255)),
                ('comapny_address', models.CharField(max_length=255)),
                ('comapny_city', models.CharField(max_length=255)),
                ('company_state', models.CharField(max_length=255)),
                ('company_zip_code', models.CharField(max_length=255)),
                ('company_phone_number', models.CharField(max_length=255)),
                ('company_emial', models.CharField(blank=True, max_length=255, null=True)),
                ('company_fax', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField()),
                ('franchise_name', models.CharField(max_length=255)),
                ('franchise_number', models.CharField(max_length=255)),
                ('franchise_address', models.CharField(max_length=255)),
                ('franchise_city', models.CharField(max_length=255)),
                ('franchise_state', models.CharField(max_length=255)),
                ('franchise_zip_code', models.CharField(max_length=255)),
                ('franchise_phone_number', models.CharField(max_length=255)),
                ('franchise_emial', models.CharField(blank=True, max_length=255, null=True)),
                ('franchise_fax', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Franchise',
                'verbose_name_plural': 'Franchises',
            },
        ),
        migrations.CreateModel(
            name='Franchise_Entity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField()),
                ('entity_number', models.IntegerField()),
                ('entity_address', models.CharField(max_length=255)),
                ('entity_city', models.CharField(max_length=255)),
                ('entity_state', models.CharField(max_length=255)),
                ('entity_zip_code', models.CharField(max_length=255)),
                ('fentity_phone_number', models.CharField(max_length=255)),
                ('entity_emial', models.CharField(blank=True, max_length=255, null=True)),
                ('entity_fax', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Franchise Entity',
                'verbose_name_plural': 'Franchise Entities',
            },
        ),
    ]