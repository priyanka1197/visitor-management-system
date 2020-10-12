from django.db import models
import datetime
# Create your models here.
# HOST MODEL
class Host(models.Model):
    id = models.AutoField
    host_name = models.CharField(max_length=50)
    host_email = models.EmailField(blank=True, null=True)
    host_phone = models.IntegerField(max_length=10)
    host_image = models.ImageField(upload_to='img/managers')
    host_desc = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    available = models.CharField(max_length=50,default='')
    current_meeting_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " : " + str(self.host_name)

# MEETING MODEL
class Meeting(models.Model):
    id = models.AutoField
    visitor_name = models.CharField(max_length=50)
    visitor_email = models.EmailField(blank=True, null=True)
    visitor_phone = models.IntegerField(max_length=10)
    visitor_permissions = models.CharField(max_length=100,null=True)
    host = models.CharField(max_length=50, default="")
    date = models.DateField(default=datetime.datetime.now())
    time_in = models.TimeField(default=datetime.datetime.now())
    time_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)+ ' : ' + str(self.visitor_name)

class guest(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50,default='Admin')
    phoneno = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    company = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    time = models.TimeField(default=datetime.datetime.now())
    adharno = models.IntegerField(null=True)
    pancardno = models.TextField(null=True)
    licenseno = models.TextField(null=True)
    image =  models.FileField(upload_to='img/image')
    adharcard=  models.FileField(upload_to='img/adhar')
    pancard =  models.FileField(upload_to='img/pan')
    license=   models.FileField(upload_to='img/license')
    containment = models.CharField(max_length=3)
    symptoms = models.CharField(max_length=3)
    history = models.CharField(max_length=3)
    family = models.CharField(max_length=3)
   
    def __str__(self):
        return str(self.id)+ ' : ' + str(self.name)
