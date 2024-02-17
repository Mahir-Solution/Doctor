# Generated by Django 5.0.1 on 2024-02-14 07:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0003_rename_patient_patient_model'),
        ('services', '0003_rename_services_services_model'),
        ('staff', '0003_rename_staff_staff_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('appointment_status', models.CharField(choices=[('waiting', 'Waiting'), ('progress_in', 'Progress In'), ('complete', 'Complete'), ('cancel', 'Cancel')], max_length=11)),
                ('note', models.TextField(null=True)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff_model', verbose_name='Doctor')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient_model', verbose_name='Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('Appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment', verbose_name='Appointment')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services_model', verbose_name='Service')),
            ],
        ),
    ]
