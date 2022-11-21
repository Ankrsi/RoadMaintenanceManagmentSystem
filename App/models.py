from django.db import models
import uuid

class ComplaintDataLocation(models.Model):
    #id=models.AutoField(primary_key=True,editable=False)
    id=models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    image=models.ImageField(upload_to='roadImage')
    latlong=models.CharField(max_length=50)
    status=models.CharField(max_length=15)
class ComplaintDataManual(models.Model):
    id=models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    addr=models.CharField(max_length=60)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    zip=models.CharField(max_length=15)
    image=models.ImageField(upload_to='roadImage')
    status=models.CharField(max_length=15)