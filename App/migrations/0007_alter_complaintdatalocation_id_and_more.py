# Generated by Django 4.0.3 on 2022-11-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_complaintdatalocation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintdatalocation',
            name='id',
            field=models.CharField(default='3F7E5', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='complaintdatamanual',
            name='id',
            field=models.CharField(default='D2E24', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]