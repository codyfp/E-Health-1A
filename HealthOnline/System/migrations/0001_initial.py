# Generated by Django 3.0.5 on 2020-04-22 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organization', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('suburb', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('Identity_Document', models.FileField(upload_to='user_<built-in function id>/Identity/')),
                ('certificate', models.FileField(upload_to='user_<built-in function id>/Certificate/')),
                ('is_doctor', models.BooleanField(default=True)),
                ('is_patient', models.BooleanField(default=False)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='System.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('suburb', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('Identity_Document', models.FileField(upload_to='user_<built-in function id>/Identity/')),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='System.Country')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='System.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('code', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('drugs', models.CharField(blank=True, max_length=400, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='System.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='System.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='System.State'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='System.Gender'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='System.State'),
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='System.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='System.Patient')),
            ],
        ),
    ]