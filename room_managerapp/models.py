from django.db import models

# Create your models here.
class RoomManager(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True)
    phone_no=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    def __str__(self):
        return "Room Manager: "+self.username