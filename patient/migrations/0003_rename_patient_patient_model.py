# Generated by Django 5.0.1 on 2024-02-13 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_blood_group_alter_patient_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='patient',
            new_name='Patient_Model',
        ),
    ]
