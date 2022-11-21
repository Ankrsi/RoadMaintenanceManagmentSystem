# Generated by Django 4.0.3 on 2022-11-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_complaintdata_id_alter_complaintdata_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintDataLocation',
            fields=[
                ('id', models.CharField(default='FCA3E', editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='roadImage')),
                ('latlong', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintDataManual',
            fields=[
                ('id', models.CharField(default='42378', editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('addr', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='roadImage')),
            ],
        ),
        migrations.DeleteModel(
            name='ComplaintData',
        ),
    ]
