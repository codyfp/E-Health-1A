# Generated by Django 2.2.12 on 2020-04-27 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0005_certificate_certificate_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='certificate_desc',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
