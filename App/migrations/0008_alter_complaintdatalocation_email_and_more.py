# Generated by Django 4.0.3 on 2022-11-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_complaintdatalocation_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintdatalocation',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complaintdatalocation',
            name='id',
            field=models.CharField(default='5DC26', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='complaintdatamanual',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complaintdatamanual',
            name='id',
            field=models.CharField(default='AE4D5', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
