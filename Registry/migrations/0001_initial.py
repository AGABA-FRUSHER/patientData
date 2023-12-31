# Generated by Django 3.2.4 on 2023-10-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('communicare_password', models.CharField(blank=True, max_length=255, null=True)),
                ('communicare_url', models.CharField(blank=True, max_length=255, null=True)),
                ('communicare_username', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by_id', models.IntegerField()),
                ('credit_period', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dicom_pacs', models.CharField(blank=True, max_length=255, null=True)),
                ('dicom_server', models.CharField(blank=True, max_length=255, null=True)),
                ('dicom_toolkit', models.CharField(blank=True, max_length=255, null=True)),
                ('instance_identifier', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('minimum_taxable_income', models.DecimalField(decimal_places=2, max_digits=19)),
                ('month_work_days', models.IntegerField()),
                ('name', models.CharField(max_length=255, unique=True)),
                ('petty_cashledger_account_id', models.BigIntegerField(blank=True, null=True)),
                ('postal_address', models.CharField(blank=True, max_length=255, null=True)),
                ('reminder_message', models.TextField()),
                ('retirement_age', models.IntegerField()),
                ('telephone', models.CharField(max_length=255)),
                ('vat_ledger_account_id', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('artson_password', models.CharField(blank=True, max_length=255, null=True)),
                ('artson_url', models.CharField(blank=True, max_length=255, null=True)),
                ('artson_username', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'branch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('administrative_contact', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('pin', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_address', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(max_length=255)),
                ('web', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('geo_area_level1name', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_area_level2name', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_area_level3name', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_area_level4name', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_area_level5name', models.CharField(blank=True, max_length=255, null=True)),
                ('iso_code2', models.CharField(max_length=255)),
                ('iso_code3', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('telephone_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeoAreaLevel1',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('geo_latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'geo_area_level1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeoAreaLevel2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('geo_latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'geo_area_level2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeoAreaLevel3',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('geo_latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'geo_area_level3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeoAreaLevel4',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('geo_latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'geo_area_level4',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeoAreaLevel5',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('geo_latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('geo_longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'geo_area_level5',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('partner_type', models.CharField(max_length=18)),
                ('phone_number', models.CharField(max_length=255)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_available', models.BooleanField()),
                ('is_cost_fixed', models.BooleanField()),
                ('is_system_defined', models.BooleanField()),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=10)),
                ('qty_per_unit', models.IntegerField()),
                ('sku', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_selling_price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegisteredPatientDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('birth_date', models.DateTimeField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=6)),
                ('id_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=9, null=True)),
                ('other_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_location', models.CharField(blank=True, max_length=255, null=True)),
                ('village', models.CharField(blank=True, max_length=255, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'registered_patient_detail',
                'managed': False,
            },
        ),
    ]
