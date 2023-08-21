# Generated by Django 4.2.4 on 2023-08-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255)),
                ('christian_names', models.CharField(max_length=255)),
                ('pob', models.CharField(max_length=255, verbose_name='place of birth')),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('nationality', models.CharField(max_length=255)),
                ('foreign_address', models.CharField(max_length=255)),
                ('foreign_address1', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('occu', models.CharField(max_length=255, verbose_name='occupation')),
                ('ppn', models.CharField(max_length=255, verbose_name='passport number')),
                ('pp_exp', models.DateField(verbose_name='passport expiry date')),
                ('pp_issue_place', models.CharField(max_length=255, verbose_name='passport place issued')),
                ('pp_issue_date', models.DateField(verbose_name='passport issued date')),
                ('arrival_date', models.DateField()),
                ('arrived_from', models.CharField(max_length=255)),
                ('arrived_via', models.CharField(max_length=255)),
                ('pov', models.CharField(max_length=255, verbose_name='purpose of visit')),
                ('imm_offr', models.CharField(max_length=255, verbose_name='immigration officer')),
                ('time_granted', models.CharField(max_length=255)),
                ('time_granted_from', models.DateField(verbose_name='from')),
                ('time_granted_to', models.DateField(verbose_name='to')),
                ('address_in_st_lucia', models.CharField(max_length=255, verbose_name='Address in St Lucia')),
                ('tel_in_st_lucia', models.CharField(max_length=255, verbose_name='Telephone in St Lucia')),
                ('means_of_support', models.CharField(max_length=255)),
                ('ticket_no', models.CharField(max_length=255, verbose_name='ticket number')),
                ('validity', models.DateField(verbose_name='valid until')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('receipt_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='receipt number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryRemarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualArrears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PortOfEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('entry_type', models.CharField(choices=[('AIR', 'AIR'), ('SEA', 'SEA')], default='AIR', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='SubsequentPermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_of_stay', models.CharField(blank=True, max_length=255)),
                ('time_granted', models.CharField(max_length=255)),
                ('time_granted_from', models.DateField(verbose_name='from')),
                ('time_granted_to', models.DateField(verbose_name='to')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubsequentPermitPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('receipt_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='receipt number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubsequentPermitRemarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
