# Generated by Django 4.2.6 on 2023-10-29 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extensions', '0017_remove_enquiry_imm_offr'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='imm_offr',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='officers', to=settings.AUTH_USER_MODEL, verbose_name='immigration officer'),
        ),
    ]
