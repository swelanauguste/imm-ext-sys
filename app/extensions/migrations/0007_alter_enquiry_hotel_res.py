# Generated by Django 4.2.4 on 2023-08-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensions', '0006_alter_enquiry_host_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='hotel_res',
            field=models.FileField(blank=True, null=True, upload_to='hotel_res_images/', verbose_name='Hotel reservations'),
        ),
    ]